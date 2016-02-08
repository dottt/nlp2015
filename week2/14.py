#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def head(file, n):
    for i, line in enumerate(open(file, 'r')):
        if n == i:
            break
        print(line.strip())
    return

def main(args):
    if len(args) > 1:
        head('hightemp.txt', int(args[1]))
    else:
        head('hightemp.txt', 3)

if __name__ == '__main__':
    main(sys.argv)
    
# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．

# $ head -3 hightemp.txt
# 高知県	江川崎	41	2013-08-12
# 埼玉県	熊谷	40.9	2007-08-16
# 岐阜県	多治見	40.9	2007-08-16
