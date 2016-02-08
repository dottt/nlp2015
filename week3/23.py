#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import grep

def regexp_section(file_name, word):
    text_list = grep.grep(file_name, word)
    for text in text_list:
        for line in text.split("\n"):
            m = re.findall('(^=+)(.*?)=+$', line)
            if m:
                print(m[0][1] + " " + str(len(m[0][0])))

def main(file_name, word):
    regexp_section(file_name, word)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        main('jawiki-country.json', 'イギリス')
    else:
        main(sys.argv[1], sys.argv[2])

# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

# 国名 2
# 歴史 2
# 地理 2
# 気候 3
# 政治 2
# 外交と軍事 2
# 地方行政区分 2
# 主要都市 3
# 科学技術 2
# 経済 2
# 鉱業 3
# 農業 3
# 貿易 3
# 通貨 3
# 企業 3
# 交通 2
# 道路 3
# 鉄道 3
# 海運 3
# 航空 3
# 通信 2
# 国民 2
# 言語 3
# 宗教 3
#  婚姻  3
# 教育 3
# 文化 2
# 食文化 3
# 文学 3
#  哲学  3
# 音楽 3
# イギリスのポピュラー音楽 4
# 映画 3
# コメディ 3
# 国花 3
# 世界遺産 3
# 祝祭日 3
# スポーツ 2
# サッカー 3
# 競馬 3
# モータースポーツ 3
# 脚注 2
# 関連項目 2
# 外部リンク 2
