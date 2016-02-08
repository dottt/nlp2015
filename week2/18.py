#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def uniq(file, n):
    dict = {}
    for i, line in enumerate(open(file, 'r')):
        dict[line] = line.split("\t")[n-1]
    for key, value in sorted(dict.items(), key=lambda x:x[1]):
        print(key, end = "")
    return

def main(args):
    if len(args) > 1:
        uniq('hightemp.txt', int(args[1]))
    else:
        uniq('hightemp.txt', 3)

if __name__ == '__main__':
    main(sys.argv)

# 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

# $ sort -k 3 hightemp.txt
# 愛知県	名古屋	39.9	1942-08-02
# 山形県	鶴岡	39.9	1978-08-03
# 山梨県	大月	39.9	1990-07-19
# 大阪府	豊中	39.9	1994-08-08
# 埼玉県	鳩山	39.9	1997-07-05
# 千葉県	茂原	39.9	2013-08-11
# 群馬県	前橋	40	2001-07-24
# 岐阜県	美濃	40	2007-08-16
# 山形県	酒田	40.1	1978-08-03
# 愛媛県	宇和島	40.2	1927-07-22
# 静岡県	佐久間	40.2	2001-07-24
# 千葉県	牛久	40.2	2004-07-20
# 愛知県	愛西	40.3	1994-08-05
# 群馬県	上里見	40.3	1998-07-04
# 群馬県	館林	40.3	2007-08-16
# 埼玉県	越谷	40.4	2007-08-16
# 山梨県	勝沼	40.5	2013-08-10
# 静岡県	天竜	40.6	1994-08-04
# 和歌山県	かつらぎ	40.6	1994-08-08
# 山梨県	甲府	40.7	2013-08-10
# 山形県	山形	40.8	1933-07-25
# 埼玉県	熊谷	40.9	2007-08-16
# 岐阜県	多治見	40.9	2007-08-16
# 高知県	江川崎	41	2013-08-12