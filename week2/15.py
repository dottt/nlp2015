#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

#行を配列に全部いれるのでメモリ的に厳しい
def tail(file, n):
    i = 0
    with open(file, 'r') as address:
        address_list = list(address)
    for i in range(len(address_list) - n, len(address_list)):
        print(address_list[i].strip())
    return

# 最初に行数を数えて、次のループで現在の行数が(行の総数-表示する行数)より大きかったら表示する
def tail2(file, n):
    len = sum(1 for l in open(file))
    for i, line in enumerate(open(file)):
        if len - n <= i:
            print(line.strip())
    return

def main(args):
    if len(args) > 1:
        #tail('hightemp.txt', int(args[1]))
        tail2('hightemp.txt', int(args[1]))
    else:
        #tail('hightemp.txt', 2)
        tail2('hightemp.txt', 2)

if __name__ == '__main__':
    main(sys.argv)

# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
# 確認にはtailコマンドを用いよ．

 # $ tail -n 2 hightemp.txt
