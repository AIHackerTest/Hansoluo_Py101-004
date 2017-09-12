# -*- coding:utf-8 -*-
# ch3 开发一个运行在Web界面，部署在本地的天气查询程序

import requests
import json

from flask import Flask, render_template, url_for, request
app = Flask(__name__)
user_data = []
url = 'https://api.seniverse.com/v3/weather/daily.json'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/query', methods = ['POST'])
def weather():
    help_info = None
    a = None
    try:
        if request.form['action'] == "历史":
            history = user_data
        elif request.form['action'] == "帮助":
            help_info = help
        elif request.form['action'] == "查询":
            a = fetchWeather(request.form['city'])
            user_data.append([a[0][0], a[0][1], a[0][2], a[0][3], a[0][4], a[0][5]])
        return render_template('home.html', **locals())
    except KeyError:
        error = 1
        return render_template('home.html', error=error)

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
        timeout=5)

    weather_info = []

    weather = json.loads(result.text)
    date = weather['results'][0]['daily'][0]["date"]
    loc = weather['results'][0]['location']["name"]
    text = weather['results'][0]['daily'][0]["text_day"]
    tem_high = weather['results'][0]['daily'][0]["high"]
    tem_low = weather['results'][0]['daily'][0]["low"]
    wind_dir = weather['results'][0]['daily'][0]["wind_direction"]
    update_date = weather['results'][0]["last_update"]
    weather_info.append([date, loc, text, tem_low, tem_high, wind_dir, update_date])

    return weather_info

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
