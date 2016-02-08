#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def uniq(file, n):
    dict = {}
    for line in open(file, 'r'):
        columns = line.split('\t')
        dict[columns[n-1]] = dict.get(columns[n-1], 0) + 1
    print(len(dict))
    return

def main(args):
    if len(args) > 1:
        uniq('hightemp.txt', int(args[1]))
    else:
        uniq('hightemp.txt', 1)

if __name__ == '__main__':
    main(sys.argv)

# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．
# 確認にはsort, uniqコマンドを用いよ．

# sortとuniqで出す方法がわからない・・
# $ cut -f1 hightemp.txt|sort -u |wc -l
# 12


# dict.get(key, keyがないときの値)
