import requests
import json
import time
import hashlib
import random

dataSK = {}

def create_headers(query,salt,sign):
    headers = {
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
        "Connection":"keep-alive",
        "Content-Length":"196" + str(len(query)),
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie":"", # 填写cookie
        "Host":"fanyi.youdao.com",
        "Origin":"http://fanyi.youdao.com",
        "Referer":"http://fanyi.youdao.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
        "X-Requested-With":"XMLHttpRequest",
        "X-Forwarded-For":"1.1.1.1", # 代理时使用，隐藏真实IP
        }
    data = {
        "i":query,
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":salt,
        "sign":sign,
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTIME",
        "typoResult":"false",
        }
    return headers,data

def get_sign(query,salt):
    s1 = 'fanyideskweb'
    s2 = 'ebSeFb%=XZ%T[KZ)c(sy!' # s2一般会定期更改
    sign = hashlib.md5((s1+query+salt+s2).encode('utf-8')).hexdigest()
    #print(sign)
    return sign

def youdao_fanyi(query):
    unixtime = str(int(time.time() * 1000))
    salt = unixtime + str(random.randint(1,10))
    sign = get_sign(query,salt)
    headers,data = create_headers(query,salt,sign)  
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    proxies = {
        'http': 'http://39.134.161.18:8080',
        'https':'https://163.28.112.100:3128'
        }
    #打开url 
    response = requests.post(url, data = data, headers = headers,
                             #proxies=proxies
                             )#response.text为str
     
    target = response.content.decode(encoding='utf-8')#[12:] # 将字符串切片
    global dataSK
    dataSK = json.loads(target) # dict
	
if __name__ == '__main__':
    while True:
        query = input('请输入要翻译的内容：')
        try:
            youdao_fanyi(query)
        except:
            print('error1：failed to open')
        if "translateResult" not in dataSK:
            print('error2：translateResult not in dataSK')
        else:
            result = dataSK["translateResult"][0][0]["tgt"]
            print('%s\n' % result)


