#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def split(file, n):
    i = 1
    outfile = 'a'
    for line in open(file, "r"):
        if i % int(n) == 0:
            outfile = chr(ord(outfile) + 1)
        with open(outfile, 'a') as out:
            print(line, file=out, end="")
        i += 1;
        out.close
    return

def main(args):
    if len(args) > 1:
        split('hightemp.txt', int(args[1]))
    else:
        split('hightemp.txt', 10)

if __name__ == '__main__':
    main(sys.argv)

# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．

# a, b, cというファイル名で作成される
# $ split -10 hightemp

# with statementを使うとクローズしなくてもよい

# with open("test.txt") as f
#     print f.read()
#    #何らかの処理
