#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def frequency_column(file, n):
    dict = {}
    for line in open(file, 'r'):
        columns = line.split('\t')
        if columns[n-1] in dict:
            dict[columns[n-1]] += 1
        else:
            dict[columns[n-1]] = 1
    for key, value in sorted(dict.items(), key=lambda x:x[1], reverse=True):
        print (str(value) + ' ' + key)
    return

def main(args):
    if len(args) > 1:
        frequency_column('hightemp.txt', int(args[1]))
    else:
        frequency_column('hightemp.txt', 1)

if __name__ == '__main__':
    main(sys.argv)
    
# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．

# $ cut -f 1 hightemp.txt|sort  |uniq -c |sort -r
#      3 群馬県
#      3 山梨県
#      3 山形県
#      3 埼玉県
#      2 静岡県
#      2 愛知県
#      2 岐阜県
#      2 千葉県
#      1 和歌山県
#      1 高知県
#      1 愛媛県
#      1 大阪府
