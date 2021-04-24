'''
Author: Gunnvant
Module generates ngram proportions from plain text files
'''

import os
import csv
from typing import Generator
import nltk
from nltk import ngrams
from nltk import word_tokenize
import string


class Ngram():
    def _ngram(self, dat, n):
        return ngrams(dat,
                      n,
                      pad_left=True,
                      pad_right=True,
                      right_pad_symbol='eos',
                      left_pad_symbol='bos')

    def ngram_generator(self, n):
        self.ngram_generator = (ngram for sent in self.data
                                for ngram in self._ngram(sent, n))

    def read_data(self, path):
        with open(path, 'r', encoding='utf-8') as infile:
            data = (word_tokenize(sent) for sent in infile.readlines())
            data = ([token.lower() for token in sent if
                     token not in string.punctuation] for sent in data)
        self.data = data
        self.path_data = path

    def _gen_header(self, sample):
        header = []
        for i in range(len(sample)):
            header.append(f"w_{i+1}")
        header.append("score")
        return header

    def dump_ngrams(self, path, file_name):
        message = '''NgramObject:should be a generator'''
        assert isinstance(self.ngram_generator, Generator), message
        freq_dist = nltk.FreqDist(self.ngram_generator)
        n_obs = sum(freq_dist.values())
        dump_name = os.path.join(path, file_name+".csv")
        with open(dump_name, mode='w', encoding="utf-8") as infile:
            writer = csv.writer(infile,
                                delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
            for idx, i in enumerate(freq_dist.items()):
                if idx == 0:
                    header = self._gen_header(i[0])
                    writer.writerow(header)
                score = i[1]/n_obs
                i = list(i[0])
                i.append(score)
                writer.writerow(i)
        print(f"Done writting file {file_name}")

