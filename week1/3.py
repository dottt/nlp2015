#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re

str="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
for i in str.split(" "):
    print(len(re.sub('[^a-zA-Z]','', i)))

# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
