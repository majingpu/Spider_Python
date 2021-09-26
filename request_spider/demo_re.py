#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

password = 'hello world IFJKLS342jkflsj'
line = "Cats are smarter than dogs"

result = re.match(r'^hello world (\w+)$', password)
print(type(result))
print(result.group(1))

result1 = re.search(r'(.*) are (.*?) .*', line)
print(type(result1))
print(result1.group(1))
print(result1.group(2))


phone = "2004-959-559 # 这是一个国外电话号码"
num1 = re.search(r'#.*$', phone)
num = re.sub(r'#.*$', "", phone)
print(num)
print(num1.group())


m = re.findall(r'\d+', phone,re.S)
print(type(m))

[print(i) for i in m if int(i) < 1000]







