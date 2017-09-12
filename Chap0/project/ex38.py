# coding:utf-8
# py2转化py3练习 ex38.py 练习列表的数据类型

ten_things = "苹果 橘子 酒 电话 电灯 糖"
print ("这还不够10个")

stuff = ten_things.split(' ')
more_stuff = ["电脑", "木瓜", "烟", "盐", "茶"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    stuff.append(next_one)

print (stuff)

print (stuff[1])
print (stuff[0])
print (stuff[-1])
print (stuff.pop())
print (' '.join(stuff))  # 本来的写法应该是stuff.join(' ') 但是python里习惯用倒装 有点类似 from sys import XXX
print ('#'.join(stuff[3:5]))