#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def wc(file):
    line_count = 0
    for line in open(file, 'r'):
     line_count += 1
    return line_count

def wc2(file):
    f = open(file, 'r')
    return len([None for l in f])

def wc3(file):
    return sum(1 for l in open(file))

def main(args):
    print(wc('hightemp.txt'))
    #print(wc2('hightemp.txt'))
    #print(wc3('hightemp.txt'))

if __name__ == '__main__':
    main(sys.argv)
    
# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．
