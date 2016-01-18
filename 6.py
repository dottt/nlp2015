#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def ngram(input, n):
    set=[]
    for c in range(0, len(input)-n+1):
        set.append(input[c:c+n])
    return set

x=ngram("paraparaparadise", 2)
y=ngram("paragraph", 2)
print('X')
print(x)
print('Y')
print(y)
print('和集合')
print(set(x)|set(y))
print(set(x).union(set(y)))
print('積集合')
print(set(x)&set(y))
print(set(x).intersection(set(y)))
print('差集合')
print(set(x)^set(y))
print(set(x).symmetric_difference(set(y)))

print('se' in set(x))
print('se' in set(y))

# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
# XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
