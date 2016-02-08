#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import grep

def regexp_category_line(file_name, word):
    text_list = grep.grep(file_name, word)
    p = re.compile('Category') # TODO: media wiki 記法
    for text in text_list:
        for line in text.split("\n"):
            if p.findall(line): # TODO: search? match? でできないか
                print(line, end = "\n")

def main(file_name, word):
    regexp_category_line(file_name, word)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        main('jawiki-country.json', 'イギリス')
    else:
        main(sys.argv[1], sys.argv[2])

# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．

# [[Category:イギリス|*]]
# [[Category:英連邦王国|*]]
# [[Category:G8加盟国]]
# [[Category:欧州連合加盟国]]
# [[Category:海洋国家]]
# [[Category:君主国]]
# [[Category:島国|くれいとふりてん]]
# [[Category:1801年に設立された州・地域]]
