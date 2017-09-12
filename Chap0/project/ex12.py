# -*- coding: utf-8 -*-
# py2转py3的练习  ex12.py
# 区别是输入语句和格式化字符串
# 这里有一个问题是，我输入名字敲的是shy，就会报错提示： name 'shy' is not defined
# 我直接敲'shy' 没有问题 
# ？？

name = input("你叫什么名字:")
age = input("你多大:")
height = input("你多高:")
weight = input("你多重:")

print ("{0}有{1}岁, {2}高, {3}重.".format(name, age, height, weight))
