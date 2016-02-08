#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import grep

def regexp_file(file_name, word):
    text_list = grep.grep(file_name, word)
    list = [];
    for text in text_list:
        for line in text.split("\n"):
            m = re.findall('ファイル:(.*?)\|', line)
            if m:
                list = list + m
    return list

def main(file_name, word):
   print(regexp_file(file_name, word))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        main('jawiki-country.json', 'イギリス')
    else:
        main(sys.argv[1], sys.argv[2])

# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．

# $ python 24.py                           [~/Dropbox/script/nlp2015/week3]
# ['Royal Coat of Arms of the United Kingdom.svg', 'CHANDOS3.jpg', 'The Fabs.JPG', 'PalaceOfWestminsterAtNight.jpg', 'Westminster Abbey - West Door.jpg', 'Edinburgh Cockburn St dsc06789.jpg', 'Canterbury Cathedral - Portal Nave Cross-spire.jpeg', 'Kew Gardens Palm House, London - July 2009.jpg', '2005-06-27 - United Kingdom - England - London - Greenwich.jpg', 'Stonehenge2007 07 30.jpg', 'Yard2.jpg', 'Durham Kathedrale Nahaufnahme.jpg', 'Roman Baths in Bath Spa, England - July 2006.jpg', 'Fountains Abbey view02 2005-08-27.jpg', 'Blenheim Palace IMG 3673.JPG', 'Liverpool Pier Head by night.jpg', "Hadrian's Wall view near Greenhead.jpg", 'London Tower (1).JPG', 'Wembley Stadium, illuminated.jpg']
