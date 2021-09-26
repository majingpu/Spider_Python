#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from lxml import etree

# 1.读取文本解析节点

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">第一个</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0"><a href="link5.html">a属性</a>
     </ul>
 </div>
'''
# 初始化生成一个Xpath解析对象
# html = etree.HTML (text)
# # 解析对象输出代码
# result = etree.tostring (html, encoding='utf-8')
# print (type (html))
# print (type (result))
#
# print (result.decode ('utf-8'))

# 2.读取html文件进行解析
# html = etree.parse ('test.html', etree.HTMLParser ())  # 指定解析器HTMLParser会根据文件修复html文件中缺失的如声明信息
# result = etree.tostring (html,encoding='utf-8')  # 解析成字节
# print(type(html))
# print (type (result))
#
# print(result.decode('utf-8'))


# 3.获取所有节点
# html = etree.parse('test.html',etree.HTMLParser())
# result = html.xpath('//*')
#
# print(type(html))
# print(type(result))
# print(result)


# 4.属性匹配
# html = etree.parse ('test.html', etree.HTMLParser ())
# result = html.xpath ('//li[@class="item-0"]/a/text()')
# result1 = html.xpath ('//li[@class]')
# result3 = html.xpath('//li/a[@href]')
# print (result)
# print (result1)
# print (result3)


# 5.多属性匹配，使用and链接
text1 = '''
<div>
    <ul>
         <li class="aaa" name="item"><a href="link1.html">第一个</a></li>
         <li class="aaa" name="fore"><a href="link2.html">second item</a></li>
     </ul>
 </div>
'''

# html = etree.HTML(text1 ,etree.HTMLParser())
# result = html.xpath('//li[@class="aaa" and @name="item"]/a/text()')
# print(result)

# 6.按序选择
text2 = """
<div>
    <ul>
         <li class="aaa" name="item"><a href="link1.html">第一个</a></li>
         <li class="aaa" name="item"><a href="link1.html">第二个</a></li>
         <li class="aaa" name="item"><a href="link1.html">第三个</a></li>
         <li class="aaa" name="item"><a href="link1.html">第四个</a></li> 
     </ul>
 </div>
"""

html = etree.HTML (text2, etree.HTMLParser ())
result = html.xpath ('//li[@class="aaa"]/a/text()')  # 获取所有li节点下的a节点内容
result1 = html.xpath ('//li[1][@class="aaa"]/a/text()')  # 获取第一个
result2 = html.xpath ('//li[last()][@class="aaa"]/a/text()')  # 获取最后一个
result3 = html.xpath ('//li[position()>2 and position()<4][contains(@class,"aaa")]/a/text()')  # 获取第三个
result4 = html.xpath ('//li[last()-2][contains(@class,"aaa")]/a/text()')  # 获取倒数第三个
print (result)
print (result1)
print (result2)
print (result3)
print (result4)

