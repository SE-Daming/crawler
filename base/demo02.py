'''
URL编码(将要搜索的信息转换为URL编码)
parse.quote()
parse.urlencode()
'''
from urllib import  parse
#普通字符串编码
url="https://www.zhihu.com/search?type=content&q="
keyword=input("请输入搜索关键词：")
url=url+parse.quote(keyword)
print(url)

#字典编码
data = {'姓名': 'Alice', 'age': 30, 'city': 'New York'}
encoded_data = parse.urlencode(data)
print(encoded_data)

