#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def cut(file):
    col1 = open('col1.txt', 'w')
    col2 = open('col2.txt', 'w')
    for line in open(file,'r'):
        print(line.split('\t')[0], file = col1);
        print(line.split('\t')[1], file = col2);
    col1.close();
    col2.close();
    return

def main(args):
    cut('hightemp.txt')

if __name__ == '__main__':
    main(sys.argv)

# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．
