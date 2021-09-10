#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import requests
import json
from lxml import etree
import re


def get_ont_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print("return status_code:{}".format(response.status_code))


def parse_page(html):
    """lxml match """
    items = re.findall('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                       + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                       + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', html, re.S)

    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def main(offset):
    url = "https://maoyan.com/board/4?offset=" + str(offset)
    html = get_ont_page(url)
    for item in parse_page(html):
        print(item)
        with open('maoyan.html', "a") as f:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    for i in range(0, 100, 10):
        main(i)
        time.sleep(1)
