#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random

def typoglycemia(input):
    result=[]
    for w in input.split(" "):
        if len(w) <= 4:
            result.append(w)
            continue
        str=w[0]
        x = [w[r] for r in range(1,len(w)-1)]
        random.shuffle(x)
        str+="".join(x)
        str+=w[-1]
        result.append(str)
    return " ".join(result)

if __name__ == '__main__':
    print(typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))

# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，
# その実行結果を確認せよ．

# random.shuffleは破壊的で返り値がないのに注意
# in-place https://ja.wikipedia.org/wiki/In-place%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0
