# -*- coding:utf-8 -*-
import os

weather_dic = {}
history_dic = {}

# 读取本地文件，分割字符，将内容存入字典
root_dir = os.path.dirname(os.getcwd())
rel_dir = os.path.join(root_dir, 'resource', 'weather_info.txt')
with open(rel_dir, 'r', encoding = 'utf8') as w:
    for info in w.readlines():
        info = info.strip()  # 去掉尾部的换行符号
        city, weather = info.split(",")
        weather_dic[city] = weather

def main():

    while True:
        user_input = str(input("请输入指令或您要查询的城市名:"))

        if user_input == "help":
            help_doc()
        elif user_input == "history":
            for city in history_dic:
                print (city, history_dic[city])
        elif user_input == "quit":
            print("显示查询历史，退出查询系统")
            for city in history_dic:
                print (city, history_dic[city])
            break
        elif user_input in weather_dic.keys():
            weather_print = weather_dic[user_input]
            history_dic[user_input] = weather_print
            print("{0}的天气状况为：{1}".format(user_input, weather_print))
        else:
            print("没有该城市信息！请输入help查看帮助文档")

# 帮助文档
def help_doc():
    print ("""
    输入城市名，查询该城市的天气；
    输入 help，打印帮助文档；
    输入 history，获取查询历史；
    输入 quit，退出天气查询系统。
    """)

if __name__ == '__main__':
    main()
