import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer
nltk.download('punkt')

stemmer = PorterStemmer()


def stem(word):
    return stemmer.stem(word)


def tokenize(sentence):
    return nltk.word_tokenize(sentence.lower())


def bag_of_words(tok_sentence, words):
    tok_sentence = [stem(w) for w in tok_sentence]

    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in tok_sentence:
            bag[idx] = 1.0

    return bag

