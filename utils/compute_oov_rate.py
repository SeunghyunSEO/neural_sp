#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2018 Kyoto University (Hirofumi Inaguma)
#  Apache 2.0  (http://www.apache.org/licenses/LICENSE-2.0)

"""Compute OOV (out-of-vocabylary) rate."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import codecs

parser = argparse.ArgumentParser()
parser.add_argument('word_count', type=str,
                    help='word count file')
parser.add_argument('dict', type=str,
                    help='dictionary file')
parser.add_argument('set', type=str,
                    help='dataset')
args = parser.parse_args()


def main():

    vocab = set([])
    with codecs.open(args.dict, 'r', encoding="utf-8") as f:
        vocab = set([])
        for line in f:
            v, idx = line.strip().split(' ')
            vocab.add(v)

    n_oovs = 0
    n_words = 0
    with codecs.open(args.word_count, 'r', encoding="utf-8") as f:
        for line in f:
            count, w = line.strip().split(' ')

            # For swbd
            if w == '(%hesitation)':
                continue

            n_words += int(count)
            if w not in vocab:
                n_oovs += int(count)

    oov_rate = float(n_oovs * 100) / float(n_words)
    print("%s: %.3f%%" % (args.set, oov_rate))


if __name__ == '__main__':
    main()
