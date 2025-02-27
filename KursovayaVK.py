import configparser
import requests
from pprint import pprint
from datetime import datetime
from tqdm import tqdm
import time


# for i in tqdm(range(10)):
#     time.sleep(0.5)

congig = configparser.ConfigParser()
congig.read("settings.ini")
vk_tk = congig["Tokens"]["vk_token"]
user_id = congig["Tokens"]["id_user"]
TOKEN_ = congig["Tokens"]["yd_token"]


class VK:
    def __init__(self, token, version='5.199'):
         self.params = {'access_token': token,'v': version}
         self.base = 'https://api.vk.com/method/'

    def get_photos(self, user_id, count = 5):
        url = f'{self.base}photos.get'
        params = {'owner_id': user_id,'count': count,'album_id': 'profile','extended': 1}

        params.update(self.params)
        response = requests.get(url, params=params)
        return response.json()

    def get_status(self, user_id):
        url = f'{self.base}status.get'
        params = {'owner_id': user_id}

        params.update(self.params)
        response = requests.get(url, params=params)
        return response.json()


    def max_size_photo(self, sizes):
        types = ["w", "z", "y", "r", "q", "p", "o", "x", "m", "s"]
        for type in types:
            for size in sizes:
                if size["type"] == type:
                    return size["url"], type


vk_connector = VK(vk_tk)
responce = vk_connector.get_photos(user_id)


photo_info = {}
items = responce['response']['items']
for item in items:
    likes = item['likes']['count']
    sizes = item['sizes']
    name = str(likes)
    url, type = vk_connector.max_size_photo(sizes)
    photo_info[name] = str({'url': url, 'type': type})
    url_jpg = item['sizes'][1]["url"]
    #print(url_jpg)


with open('test_write.txt', "w", encoding = "utf-8") as f:
    for photo in photo_info:
        f.write(photo_info[name])
        f.write(str(photo_info[name][0]) + '\n')
        print("\n".join(map(str, photo_info)), file=f)

class YD:
    def __init__(self, token):
        self.params = {'access_token': TOKEN_, 'v': version}
        print('создался ЯД')

    def folder_creation(folder_name):
        """Создаёт папку на Яндекс Диске"""
        url = f'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = {'Content-Type': 'application/json',
                   'Authorization': f'OAuth+TOKEN_'}
        params = {'path': folder_name, 'overwrite': 'false'}
        response = requests.put(url=url, headers=headers, params=params)
        print(response)

        folder_creation('Photos')

    def upload_file(self, path, url):
        #Скачивание файла из интернета на Диск
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload?url=https://sun9-64.userapi.com/s/v1/if2/7XjpgFYihljZ1Au22hjS93aHy0T9WT2RVMEIbmWWNppTqsJVLIEqC7uuuCQrBaIK6Lv_2ciyDfyQhbaNek8TTk9i.jpg?quality=96&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1280x1707,1440x1920,1536x2048&from=bu&cs=130x173&path=https://disk.yandex.ru/client/disk/Photos"
        headers = {'Content-Type': 'application/json','Authorization': f'OAuth+TOKEN_'}
        params = {'path': f'Photos','url':  link}

        response = requests.post(url=url, headers=headers, params=params)
        if response.status_code != 202:
            print(f'Ошибка на сервере. Код ошибки: {response.status_code}')
        else:
            print(response)








