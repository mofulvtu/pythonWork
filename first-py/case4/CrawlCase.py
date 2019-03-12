"""
   desc: 爬取PM2.5数据
   author: Liuzg
   date: 2019/03/12
"""

import requests


def get_html_text(url):
    """
        返回url文本
    """
    r = requests.get(url, timeout=30)
    return r.text


def main():
    city_pinyin = input("请输入城市拼音：")
    url = "http://pm25.in/" + city_pinyin

    url_text = get_html_text(url)
    print(url_text)


if __name__ == '__main__':
    main()
