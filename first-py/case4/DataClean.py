"""
   desc: 爬取PM2.5数据
         BeautifulSoup4 解析html
         自动获取所有城市的AQI
         数据分析 pandas
         保存到csv
         pandas 数据清洗

   author: Liuzg
   date: 2019/03/15
"""

import pandas as pd
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


def main():
    """
        主函数
    """
    aqi_data = pd.read_csv("china_cities_aqi.csv")
    print("基本信息：")
    print(aqi_data.info())

    print("数据预览：")
    print(aqi_data.head())

    # 数据清洗
    # 去除数据为0的数据
    aqi_data = aqi_data[aqi_data['AQI'] > 0]

    # 基本统计
    print("AQI最大值：{}".format(aqi_data['AQI'].max()))
    print("AQI最小值：{}".format(aqi_data['AQI'].min()))
    print("AQI平均值：{}".format(aqi_data['AQI'].mean()))
    print("AQI平均值：{}".format(aqi_data['AQI'].mean()))

    # Top 50
    top50_cities = aqi_data.sort_values(by=['AQI']).head(50)
    # 可视化
    top50_cities.plot(kind='bar', x='City', y='AQI', title='空气质量最好的50城市', figsize=(20, 10))

    # 存入csv
    top50_cities.to_csv("top50_aqi.csv", index=False)
    plt.savefig('top50_aqi.png')
    plt.show()


if __name__ == '__main__':
    main()
