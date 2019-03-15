"""
   desc: 爬取PM2.5数据
         BeautifulSoup4 解析html
         自动获取所有城市的AQI
         数据分析 pandas
         保存到csv

   author: Liuzg
   date: 2019/03/15
"""

import pandas as pd


def main():
    """
        主函数
    """
    aqi_data = pd.read_csv("china_cities_aqi.csv")
    print("基本信息：")
    print(aqi_data.info())

    print("数据预览：")
    print(aqi_data.head())

    # 基本统计
    print("AQI最大值：{}".format(aqi_data['AQI'].max()))
    print("AQI最小值：{}".format(aqi_data['AQI'].min()))
    print("AQI平均值：{}".format(aqi_data['AQI'].mean()))
    print("AQI平均值：{}".format(aqi_data['AQI'].mean()))

    # Top 10
    top10_cities = aqi_data.sort_values(by=['AQI']).head(10)
    print("AQI Top 10 cities:")
    print(top10_cities)

    # Bottom 10 方式一
    bottom10_cities = aqi_data.sort_values(by=['AQI']).tail(10)
    print("AQI Bottom 10 cities:")
    print(bottom10_cities)

    # Bottom 10 方式二
    bottom10_cities = aqi_data.sort_values(by=['AQI'], ascending=False).head(10)
    print("AQI Bottom 10 cities:")
    print(bottom10_cities)

    # 存入csv
    top10_cities.to_csv("top10_aqi.csv", index=False)
    bottom10_cities.to_csv("bottom10_aqi.csv", index=False)


if __name__ == '__main__':
    main()
