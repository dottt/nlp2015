#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

str="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
n=[1,5,6,7,8,9,15,16,19]
d={}
for i,word in enumerate(str.split(" ")): #1
    if i+1 in n: #2
        d[word[0]] = i+1
    else:
        d[word[0:2]] = i+1 #3
print(d)

# 04. 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

# 1. enumerateという関数に配列を食わせるとindexもとれてよい
# 2. リストに要素があるかどうかを探すにはif A in Bでよい
# 3. word[0]+word[1]でもいいけどかっこよくスライスで
