# -*- coding:utf-8 -*-
import requests
import json
import datetime
import time

def main():
    start_time = input("请输入查询时间(格式如2015/10/21 16:30：00)：")
    a = datetime.datetime.strptime(start_time, "%Y/%m/%d %H:%M:%S")
    while datetime.datetime.now() < a:
        time.sleep(1)

    weather_inqury()

url = 'https://api.seniverse.com/v3/weather/daily.json'

def fetchWeather(location, unit, start, days):
    result = requests.get(
        url,
        params={
        'key': "19e64sczvm2iz7yp",
        'location': location,
        'language': "zh-Hans",
        'unit': unit,
        'start': start,
        'days': days
        },
        timeout=1)

    weather_info = []

    weather = json.loads(result.text)
    loc = weather['results'][0]['location']['name']
    update = weather['results'][0]['last_update']
    for i in range(int(days)):
        date = weather['results'][0]['daily'][i]["date"]
        loc = weather['results'][0]['location']["name"]
        text = weather['results'][0]['daily'][i]["text_day"]
        tem_high = weather['results'][0]['daily'][i]["high"]
        tem_low = weather['results'][0]['daily'][i]["low"]
        wind_dir = weather['results'][0]['daily'][i]["wind_direction"]
        update_date = weather['results'][0]["last_update"]
        weather_info.append([date, loc, text, tem_low, tem_high, wind_dir, update_date])

    return weather_info

def weather_inqury():
    user_data = []

    # 与用户进行交互
    try:
        while True:
            user_input = str(input("请输入指令或您要查询的城市名:"))

            if user_input == "help":
                help_doc()
            elif user_input == "history":
                for i in user_data:
                    print("{}, {} 天气 {}, 温度 {}~{}度, 风向{}.".format(i[0],
                        i[1], i[2], i[3], i[4], i[5]))
            elif user_input == "quit":
                    exit(0)
            else:
                # 根据用户输入获取用户需要天气数据
                b = input("请输入温度单位f或者c:")
                c = input("请输入起始时间（0：今天,1：昨天）:")
                d = input("请输入查看天数（可选参数1,2,3）：")
                a = fetchWeather(user_input, b, c, d)

                for i in a:
                    print("{}, {} 天气 {}, 温度 {}~{}度, 风向{}.".format(i[0],
                        i[1], i[2], i[3], i[4], i[5]))
                    # 储存用户的查询数据
                    user_data.append([i[0], i[1], i[2], i[3], i[4], i[5]])

                print("更新时间：{0}".format(a[0][6]))

    except KeyError:
        print("您的输入无法识别")

def help_doc():
    print("""
    输入城市名，查询该城市的天气；
    输入 help，打印帮助文档；
    输入 history，获取查询历史；
    输入 quit，退出天气查询系统。
    """)

if __name__ == '__main__':
    main()
