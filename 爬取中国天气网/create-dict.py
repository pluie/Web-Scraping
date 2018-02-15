import pickle
from pypinyin import lazy_pinyin



f = open('中国天气网城市代码.txt')

city_dict = {}

for line in f.readlines():
    if line != '\n': #如果不是空行
        #以'='切片，同时去除'\n'
        (city_code,city_name) = line.strip('\n').split('=',1)
        city_dict.setdefault(city_name,city_code)
        #将城市名转为拼音
        city_pinyin = lazy_pinyin(city_name)[0] + lazy_pinyin(city_name)[1]
        city_dict.setdefault(city_pinyin,city_code)

f.close()

fileoutput = open('city-dict.pkl','wb')
pickle.dump(city_dict,fileoutput)
fileoutput.close()
        
        
