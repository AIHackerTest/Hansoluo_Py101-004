#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 中文编码问题，需要更改notepad++的默认编码设置，目前默认是UTF-8，要改成ANSI，已在首选项中完成设置
# 应该下一本电子版放在kindle里随时看 这样就不用带书了

# py2转py3的练习  ex14.py
# 跟ex12同样的问题 input输入字符串类型就报错
# 实际要解决的问题是： 如何切换和运行不同版本的python？

# 运行python程序之前先检查python的版本 结果发现python-3并没有什么用
# 这段程序用python2与python3运行是一样的 实际上就是python2，还没有切换到python3
# 在python3.6 IDE 运行 结果不会传入数据

import sys
print (sys.version)

from sys import argv

script, user_name = argv
prompt = '>'

print ("Hi, {0}, I'm the {1} script.".format(user_name, script))
print ("I'd like to ask you a few questions.")
print ("Do you like me {0}".format(user_name))
likes = input(prompt)

print ("where do you live {0}?".format(user_name))
lives = input(prompt)

print ("what kind computer do you have?")
computer = input(prompt)

print ("""
# You said '{0}' about like me.
# You live in '{1}'.
# And you have a '{2}' computer.
""".format(likes, lives, computer))
