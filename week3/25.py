#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import grep

def category_name(file_name, word):
    text_list = grep.grep(file_name, word)
    dist = {}
    for text in text_list:
        for line in text.split("\n"):
            p = re.compile('\A\|(.*?) = (.*?)\Z'); # TODO fix
            m = p.match(line)
            if m != None:    
                dist[m.group(1)] = m.group(2)
    return dist

def main(file_name, word):
   print(category_name(file_name, word))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        main('jawiki-country.json', 'イギリス')
    else:
        main(sys.argv[1], sys.argv[2])

# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

#{'GDP順位MER': '5', '確立年月日1': '[[927年]]／[[843年]]', '略名': 'イギリス', '公式国名': '{{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>', '確立形態2': '[[グレートブリテン王国]]建国<br />（[[連合法 (1707年)|1707年連合法]]）', '面積順位': '76', '標語': '{{lang|fr|Dieu et mon droit}}<br/>（[[フランス語]]:神と私の権利）', '国際電話番号': '44', '面積値': '244,820', '首都': '[[ロンドン]]', '確立年月日4': '[[1927年]]', '最大都市': 'ロンドン', 'GDP順位': '6', '首相等氏名': '[[デーヴィッド・キャメロン]]', 'GDP統計年元': '2012', '公用語': '[[英語]]（事実上）', '人口統計年': '2011', '人口値': '63,181,775<ref>[http://esa.un.org/unpd/wpp/Excel-Data/population.htm United Nations Department of Economic and Social Affairs>Population Division>Data>Population>Total Population]</ref>', 'GDP/人': '36,727<ref name="imf-statistics-gdp" />', '元首等肩書': '[[イギリスの君主|女王]]', '日本語国名': 'グレートブリテン及び北アイルランド連合王国', '人口順位': '22', '確立形態4': "現在の国号「'''グレートブリテン及び北アイルランド連合王国'''」に変更", '元首等氏名': '[[エリザベス2世]]', 'GDP値': '2兆3162億<ref name="imf-statistics-gdp" />', 'GDP値MER': '2兆4337億<ref name="imf-statistics-gdp" />', 'GDP統計年MER': '2012', '首相等肩書': '[[イギリスの首相|首相]]', '建国形態': '建国', 'GDP統計年': '2012', '人口密度値': '246', '通貨コード': 'GBP', '位置画像': 'Location_UK_EU_Europe_001.svg', '確立年月日3': '[[1801年]]', '国章画像': '[[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]', 'ccTLD': '[[.uk]] / [[.gb]]<ref>使用は.ukに比べ圧倒的少数。</ref>', '人口大きさ': '1 E7', '通貨': '[[スターリング・ポンド|UKポンド]] (&pound;)', '面積大きさ': '1 E11', 'GDP値元': '1兆5478億<ref name="imf-statistics-gdp">[http://www.imf.org/external/pubs/ft/weo/2012/02/weodata/weorept.aspx?pr.x=70&pr.y=13&sy=2010&ey=2012&scsm=1&ssd=1&sort=country&ds=.&br=1&c=112&s=NGDP%2CNGDPD%2CPPPGDP%2CPPPPC&grp=0&a= IMF>Data and Statistics>World Economic Outlook Databases>By Countrise>United Kingdom]</ref>', '夏時間': '+1', '国歌': '[[女王陛下万歳|神よ女王陛下を守り給え]]', '国旗画像': 'Flag of the United Kingdom.svg', '注記': '<references />', '確立形態1': '[[イングランド王国]]／[[スコットランド王国]]<br />（両国とも[[連合法 (1707年)|1707年連合法]]まで）', '時間帯': '±0', 'ISO 3166-1': 'GB / GBR', '国章リンク': '（[[イギリスの国章|国章]]）', '確立年月日2': '[[1707年]]', '水面積率': '1.3%', '確立形態3': '[[グレートブリテン及びアイルランド連合王国]]建国<br />（[[連合法 (1800年)|1800年連合法]]）'}