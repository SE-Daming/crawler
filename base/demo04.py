
'''
网络文件的下载
request.urlretrieve(url,file_name)
'''
from urllib import  request
url='https://th.bing.com/th/id/OIP.j3ljO7ywZIrrXE_JEmKBTgHaHa?pid=ImgDet&w=197&h=197&c=7'
#下载到同级下并指定文件名称(可以不存在)
request.urlretrieve(url,'demo04.jpg')

#下载到指定的文件夹中
'''
注意fileName的格式  
    ./当前目录的路径
    ../父目录的路径
    /根目录
注意fileName必须存在
'''
request.urlretrieve(url=url,filename='../base-img/demo04.jpg')


