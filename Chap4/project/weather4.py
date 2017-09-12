# coding:utf-8

# 使用 SQLite 存储天气数据 +
## 导入SQlite +
## 和 SQLite 进行基本的交互 +
### 和 SQLite 数据库建立连接？ +
### 在 SQLite 中建立游标对象？ +
### 借助游标执行 SQL 语句？
## 将API的数据返回储存到SQlite
### 查询再存储的方式实现 +
### 爬取整个数据 -

# 用户可通过 Web 页面的用户更正按钮，更正天气数据到数据库 +
## 实现更正功能 +
## 格式限定 +

# 如果在5分钟以内查询相同的数据, 不用通过 API 访问远程数据源（较难，选做）

# 可记录多个用户不同的查询历史（较难，选做）

# 使用 Flask 的扩展 Flask-SQLAlchemy 来替代 sqlite3 模块

import requests
import json
import sqlite3

from flask import Flask, render_template, url_for, request
app = Flask(__name__)
user_data = []
url = 'https://api.seniverse.com/v3/weather/daily.json'

conn = sqlite3.connect(":memory:", check_same_thread = False)
c = conn.cursor()
c.execute('''CREATE TABLE weather
            (date, loc, text, tem_low, tem_high, wind_dir, update_date)''')

def database(user_query):
    weather_info = []
    a = (str(user_query),)
    c.execute("SELECT * FROM weather WHERE loc= ?", a)
    b = c.fetchone()

    if b:
        weather_info = b
    else:
        weather_data = fetchWeather(user_query)
        c.executemany("INSERT INTO weather VALUES (?, ?, ?, ?, ?, ?, ?)", weather_data)
        c.execute("SELECT * FROM weather WHERE loc= ?", a)
        weather_info = c.fetchone()

    conn.commit()
    return weather_info

def update_data(user_update):
    a = user_update.split(' ')
    c.execute("UPDATE weather SET text=? WHERE loc=?", (a[1], a[0]))
    conn.commit()

def fetchWeather(location):
    result = requests.get(
        url,
        params={
            'key': "19e64sczvm2iz7yp",
            'location': location,
            'language': "zh-Hans",
            'unit': "c",
            'start': "0",
            'days': "1"
        },
        timeout=1)

    weather_info = []

    weather = json.loads(result.text)
    date = weather['results'][0]['daily'][0]["date"]
    loc = weather['results'][0]['location']["name"]
    text = weather['results'][0]['daily'][0]["text_day"]
    tem_high = weather['results'][0]['daily'][0]["high"]
    tem_low = weather['results'][0]['daily'][0]["low"]
    wind_dir = weather['results'][0]['daily'][0]["wind_direction"]
    update_date = weather['results'][0]["last_update"]
    weather_info.append(
        [date, loc, text, tem_low, tem_high, wind_dir, update_date])

    return weather_info

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/query', methods = ['POST'])
def weather():
    try:
        if 'action2' in  request.form.keys():
            history = user_data
        elif 'action3' in  request.form.keys():
            help_info = 1
        elif 'action1' in  request.form.keys():
            a = database(request.form['city'])
            user_data.append(
                [a[0], a[1], a[2], a[3], a[4], a[5]])
        elif 'action4' in request.form.keys():
            b = request.form['city'].split(' ')
            c = ['晴', '大雨', '中雨', '小雨', '阴',
                '多云', '大雪', '小雪', '雷阵雨', '雨夹雪']
            if b[1] in c:
                update_data(request.form['city'])
                update = 1
            else:
                wrong_input = 1
        return render_template('home.html', **locals())
    except KeyError:
        error = 1
        return render_template('home.html', error=error)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
    c.close()
    conn.close()
