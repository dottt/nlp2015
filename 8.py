#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re

def cipher(input):
    for i in range(0,len(input)):
        print (re.sub('[a-z]',chr(219 - ord(input[i])), input[i]), end="")
        
if __name__ == '__main__':
    cipher("This is a Pen.")
    
# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

# python3だとendを指定できる
# 2to3 -w でひたすらpython3化した
