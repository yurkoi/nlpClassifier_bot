import torch
import torch.nn as nn

from nltk_module import tokenize, bag_of_words


class Model1(nn.Module):
    def __init__(self, input_size, hidden_layers, output_classes):
        super(Model1, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_layers)
        self.l2 = nn.Linear(hidden_layers, hidden_layers)
        self.l3 = nn.Linear(hidden_layers, hidden_layers)
        self.l4 = nn.Linear(hidden_layers, output_classes)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        out = self.relu(out)
        out = self.l4(out)

        return out


def sentense_to_prob(sentense, all_words, tags, model):
    sentence = tokenize(sentense)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    return prob, tag
