#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import grep

def regexp_category(file_name, word):
    text_list = grep.grep(file_name, word)
    list = []
    for text in text_list:
        for line in text.split("\n"):
            m = re.fullmatch('\[\[Category:((.*?)(\|.*?)?)\]\]', line)
            if m:
                list.append(m.group(2))
    return list

def main(file_name, word):
    print(regexp_category(file_name, word))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        main('jawiki-country.json', 'イギリス')
    else:
        main(sys.argv[1], sys.argv[2])

# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

# $ python 22.py
# ['イギリス', '英連邦王国', 'G8加盟国', '欧州連合加盟国', '海洋国家', '君主国', '島国', '1801年に設立された州・地域']
