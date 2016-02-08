#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
from pprint import pprint

def grep(file_name, word):
    list = [];
    for line in open(file_name):
        json_data = json.loads(line)
        if word == json_data['title']:
            list.append(json_data['text'])
    return list;

def main(file_name, word):
    list = grep(file_name, word)
    for line in list:
        print(line, end = "\n")
    return

if __name__ == '__main__':
    if len(sys.argv) < 2:
        main('jawiki-country.json', 'イギリス')
    else:
        main(sys.argv[1], sys.argv[2])

# 20. JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．
