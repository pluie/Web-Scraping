import requests
import pickle
import json
import time

dataSK = {}

def get_weather():
    #导入字典
    fileinput = open('city-dict.pkl','rb')
    city_dict = pickle.load(fileinput)
    fileinput.close()
    city_name = input('输入城市：')
    city_code = city_dict[city_name]
    
    #创建headers
    referer = 'http://www.weather.com.cn/weather1d/' + city_code + '.shtml'
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Referer": referer,
	"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
	"Host":"d1.weather.com.cn",
        }
    
    unix_time = str(int(time.time() * 1000))
    url = 'http://d1.weather.com.cn/sk_2d/' + city_code + '.html?_=' + unix_time 
    response = requests.get(url, headers = headers) # 打开url
    target = response.content.decode(encoding='utf-8')[12:] # 将字符串切片
    global dataSK
    dataSK = json.loads(target) # json得到字典

if __name__ == '__main__':
    while True:
        get_weather()
        #print(type(dataSK))
        #print(dataSK)
        #打印结果
        print('城市：%s\n日期：%s' % (dataSK['cityname'],dataSK['date']))
        print('更新时间：%s\n' % dataSK['time'])
        print('温度：%s\n风力：%s%s\n相对湿度：%s\n实时空气质量指数（AQI）：%s\n' % (dataSK['temp'],dataSK['WD'],dataSK['WS'],dataSK['sd'],dataSK['aqi']))
        if dataSK['rain'] != '0.0' or dataSK['rain24h'] != '0':
            print('降雨量：%s，24小时降雨量：%s' % (dataSK['rain'],dataSK['rain24h']))

        input('任意键继续...')
        print('\n')

