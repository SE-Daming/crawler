'''
解析本地HTML  tree.xpath()
'''
from lxml import etree
#解析HTML得到ElementTree对象（整个HTML的结构，可以用来访问和操作HTML的元素、属性和文本）
tree=etree.parse('demo03.html')
#匹配该对象的标签
'''
xpath基本语法:
    1.路径查询
    //：查找所有子孙节点，不考虑层级关系
    / ：找直接子节点
    2.谓词查询
    //div[@id]
    //div[@id="maincontent"]
    3.属性查询
    //@class
    4.模糊查询
    //div[contains(@id, "he")]
    //div[starts‐with(@id, "he")]
    5.内容查询
    //div/h1/text()
    6.逻辑运算
    //div[@id="head" and @class="s_down"]
    //title | //price
'''
#得到符合xpath的元素
data_list=tree.xpath('//div[@class="list"]/ul/li')

