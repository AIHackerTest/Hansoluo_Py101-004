#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ���ı������⣬��Ҫ����notepad++��Ĭ�ϱ������ã�ĿǰĬ����UTF-8��Ҫ�ĳ�ANSI��������ѡ�����������
# Ӧ����һ�����Ӱ����kindle����ʱ�� �����Ͳ��ô�����

# py2תpy3����ϰ  ex14.py
# ��ex12ͬ�������� input�����ַ������;ͱ���
# ʵ��Ҫ����������ǣ� ����л������в�ͬ�汾��python��

# ����python����֮ǰ�ȼ��python�İ汾 �������python-3��û��ʲô��
# ��γ�����python2��python3������һ���� ʵ���Ͼ���python2����û���л���python3
# ��python3.6 IDE ���� ������ᴫ������

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
