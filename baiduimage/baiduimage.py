import requests
import os
import time
import re


def create_params(scroll, keyword):
    unix_time = str(int(time.time()*1000))
    params = {
        unix_time: "",
        "adpicid": "",
        "cl": 2,
        "ct": 201326592,
        "expermode": "",
        "face": 0,
        "fp": "result",
        "fr": "",
        "gsm": "3c",
        "height": "",
        "ic": 0,
        "ie": "utf-8",
        "ipn": "rj",
        "is": "",
        "istype": 2,
        "lm": -1,
        "nc": 1,
        "oe": "utf-8",
        "pn": scroll,
        "qc": "",
        "queryWord": keyword,
        "rn": 30,
        "s": "",
        "se": "",
        "st": -1,
        "tab": "",
        "tn": "resultjson_com",
        "width": "",
        "word": keyword,
        "z": "",
        }
    
    headers = {
        "X-Forwarded-For":"1.1.1.1"
        }

    proxies = {
        "http": "http://124.234.157.228:80",
        "https": "https://219.234.181.194:33695"
        }
    
    return params

def get_baidu(page, params):
    url = "https://image.baidu.com/search/acjson"
    
    response = requests.get(url, params=params)#.json().get('data')[0].get("thumbURL")
    try:
        target = response.content.decode(encoding='utf-8')
    except:
        return []
    pattern = re.compile('"thumbURL":"(.*?)",')
    url_list = re.findall(pattern, target)
    #print(url_list)

    return url_list

def get_srcimg(page, keyword):
    global count

    params = create_params(page, keyword)
    lists = get_baidu(page, params)
    
    for item in lists:
        try:
            img_data = requests.get(item, timeout=10).content
            file_name = "img_" + str(count).zfill(8) + ".jpg"
            path = os.path.join(keyword, file_name)
            with open(path, "wb") as f:
                f.write(img_data)
                print("save image", file_name)
                count += 1
        except requests.exceptions.ConnectionError:
            print('can not download')
            continue

def mkdir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        return True
    else:
        print("failed, folder exist.")

        return False

def main():
    pages = 400
    keyword = "壁纸"

    ret = mkdir(keyword)
    if ret == False:
        return
    for page in range(30, (1+pages)*30, 30):
        get_srcimg(page, keyword)

if __name__ == "__main__":
    count = 0
    main()


