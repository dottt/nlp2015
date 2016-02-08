#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def expand(file):
    for line in open(file, 'r'):
        print(line.replace("\t", " "), end = "");
    return

def main(args):
    expand('hightemp.txt')

if __name__ == '__main__':
    main(sys.argv)

# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，
# trコマンド，もしくはexpandコマンドを用いよ     
