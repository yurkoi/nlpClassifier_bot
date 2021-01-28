import json

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset

from model_utils import Model1
from nltk_module import tokenize, stem, bag_of_words

with open('data/patterns_info.json', 'r') as file:
    intents = json.load(file)

all_words = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)

    for pattern in intent['patterns']:
        words = tokenize(pattern)
        all_words.extend(words)
        xy.append((words, tag))

ignore_symbols = ['!', '?', '.', ',', '`']
all_words = [stem(w) for w in all_words if w not in ignore_symbols]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

X_train = []
y_train = []

for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)

    label = tags.index(tag)
    y_train.append(label)

X_train = np.array(X_train)
y_train = np.array(y_train)


class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(X_train)
        self.x_samples = X_train
        self.y_samples = y_train

    def __getitem__(self, item):
        return self.x_samples[item], self.y_samples[item]

    def __len__(self):
        return self.n_samples


# Hyperparameters
batch_size = 16
hidden_size = 16
output_size = len(tags)
input_size = len(X_train[0])
learning_rate = 1e-3
num_epochs = 1200

dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = Model1(input_size=input_size, hidden_layers=hidden_size, output_classes=output_size).to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(device)

        outputs = model(words)
        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 50 == 0:
            print(f'epoch {epoch + 1}/{num_epochs}, loss={loss.item():.4f} ')

data = {
    'model_state': model.state_dict(),
    'input_size': input_size,
    'output_size': output_size,
    'hidden_size': hidden_size,
    'all_words': all_words,
    'tags': tags
}

FILE = 'data/data.pth'
torch.save(data, FILE)  # into pickle

print(f'training complete, data saved to {FILE}')
