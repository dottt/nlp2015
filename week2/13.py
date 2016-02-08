#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def paste(file1, file2):
    with open(file1, 'r') as col1:
        col1_list = list(col1)
    with open(file2, 'r') as col2:
        col2_list = col2.readlines()
    # list(f)とf.readline()は同じ
    out = open ('out.txt', 'w')
    #for i in range(0, len(col1_list) if len(col1_list) > len(col2_list) else len(col2_list)):
    #    print(col1_list[i].strip() + "\t" + col2_list[i].strip(), file = out);
    for (a,b) in zip(col1_list, col2_list):
        print(a.strip() + "\t" + b.strip(), file = out);
    out.close()
    return

def main(args):
    if len(args) > 2:
        paste(args[1], args[2])
    else:
        paste('col1.txt', 'col2.txt')

if __name__ == '__main__':
    main(sys.argv)
    
# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
# 確認にはpasteコマンドを用いよ．

# $ paste col1.txt col2.txt
# 高知県	江川崎
# 埼玉県	熊谷
# 岐阜県	多治見
# 山形県	山形
# 山梨県	甲府
# 和歌山県	かつらぎ
# 静岡県	天竜
# 山梨県	勝沼
# 埼玉県	越谷
# 群馬県	館林
# 群馬県	上里見
# 愛知県	愛西
# 千葉県	牛久
# 静岡県	佐久間
# 愛媛県	宇和島
# 山形県	酒田
# 岐阜県	美濃
# 群馬県	前橋
# 千葉県	茂原
# 埼玉県	鳩山
# 大阪府	豊中
# 山梨県	大月
# 山形県	鶴岡
# 愛知県	名古屋
