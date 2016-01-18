#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def ngram (input, n):
    c=[]
    w=[]
    if isinstance(input, str):
        for i in range(0, len(input.split(' '))-n+1):
            print(input.split(' ')[i:i+n])
        for word in input.split(' '):
            for c in range(0, len(word)-n+1):
                print(word[c:c+n])
    elif isinstance(input, list):
        for i in range(0, len(input)-n+1):
            print(input[i:i+n])
        for word in input:
            for c in range(0, len(word)-n+1):
                print(word[c:c+n])
    else:
        print("error")

if __name__ == '__main__':
    ngram("I am an NLPer", 2)
    ngram(['I','am','an','NLPer'], 2)

# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

# isintance(var, type)で型判別ができる
