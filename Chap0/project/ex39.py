# coding:utf-8
# py2转py3练习 ex39.py 字典
# 首选项设置中语言里可将TAB替换为空格，节省时间
# 反向缩进的快捷键是啥？

movies = {
    '花样年华': '王家卫',
    '刺杀聂隐娘': '侯孝贤',
    '英雄': '张艺谋',
    '卧虎藏龙': '李安',
    '一一': '杨德昌'
}

directors = {
    '王家卫': '花样年华',
    '候孝贤': '刺杀聂隐娘',
    '张艺谋': '英雄'
}

directors['李安'] = '卧虎藏龙'
directors['杨德昌'] = '一一'

print ('-'*10)
print ("李安的电影：", directors['李安'])
print ("王家卫的电影：", directors['王家卫'])

print ('-'*10)
print ("卧虎藏龙的导演：", movies[directors['李安']])
print ("花样年华的导演：", movies[directors['王家卫']])

print ('-'*10)
for movie, director in movies.items():
    print ("{0} 的导演是{1}".format(movie, director))

print ('-'*10)
director = directors.get('贾樟柯', None)  # 创建了新的映射关系，并获取value值None赋给了变量director

#print (directors['贾樟柯'])  
# 第一次报错是因为之前写错了，将字典directors赋值了None，是个空字典，再调用时，报错TypeError: 'NoneType' object is not subscriptable
# 改成新的变量director后，报错Keyerror: '贾樟柯'。这是因为在读取字典的key和value时，如果key不存在，就会引发该错误
# get的创建是局部短暂的，只形成在上一行代码中 
# 改成以下代码用来测试
print (directors.get('贾樟柯')) 
print (directors) 


if not director:
    print ("没有贾樟柯的电影")

movie = movies.get('小武', '不知道')
print ("小武的导演：{0}".format(movie))
