# coding:utf-8

import requests
import json


def get_simple_weather(town_id):
    url = 'http://tj.nineton.cn/Heart/index/all?city={}'.format(town_id)
    print(url)
    json_str = requests.get(url).text

    ##print(jsonStr)
    data = json.loads(json_str)
    weather = data['weather'][0]

    print('city', weather['city_name'])
    print('text', weather['now']['text'])
    print('temperature', weather['now']['temperature'])
    result = '{city}今天{text}，最近一个小时的温度显示为{temperature}°！'.format(
        city=weather['city_name'], text=weather['now']['text'], temperature=weather['now']['temperature'])
    return result


def get_town_id(city_str=None):
    with open('.\city_code.json', 'r', encoding='utf-8') as load_f:
        load_list = json.load(load_f)
    for item in load_list:
        if item.get('cityName') == city_str or item.get('townName') == city_str:
            return item.get('townID')


def get_data(city_str):
    town_id = get_town_id(city_str)
    return get_simple_weather(town_id)


def main():
    town_id = get_town_id('北京')
    get_simple_weather(town_id)


if __name__ == '__main__':
    main()
