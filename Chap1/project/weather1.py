# -*- coding:utf-8 -*-
import os
import csv

def main():

    user_data = []

    while True:
        user_input = str(input("请输入指令或您要查询的城市名:"))
        if user_input == "help":
            help_doc()
        elif user_input == "history":
            for i in user_data:
                print(i[0], i[1])
        elif user_input == "quit":
            exit(0)
        else:
            c = get_data(user_input)
            user_data.append([user_input, c])

def get_data(a):
    root_dir = os.path.dirname(os.getcwd())
    rel_dir = os.path.join(root_dir, 'resource', 'weather_info.csv')
    w_file = open(rel_dir, 'r', encoding = 'utf8')
    w_reader = csv.reader(w_file)
    w_data = list(w_reader)

    for row in w_data:
        if a == row[0]:
            print("{0}的天气为：{1}".format(a, row[1]))
            b = row[1]

    return b

def help_doc():
    print ("""
    输入城市名，查询该城市的天气；
    输入 help，打印帮助文档；
    输入 history，获取查询历史；
    输入 quit，退出天气查询系统。
    """)

if __name__ == '__main__':
    main()
