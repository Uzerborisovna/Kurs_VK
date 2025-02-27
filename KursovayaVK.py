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
    print(url_jpg)


with open('test_write.txt', "w", encoding = "utf-8") as f:
    for photo in photo_info:
        f.write(photo_info[name])
        f.write(str(photo_info[name][0]) + '\n')
        print("\n".join(map(str, photo_info)), file=f)

class YD:
    def __init__(self, token):
        self.params = {'access_token': token, 'v': version}
        print('создался ЯД')

    def folder_creation(folder_name):
        """Создаёт папку на Яндекс Диске"""
        url = f'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = {'Content-Type': 'application/json',
                   'Authorization': f'OAuth {TOKEN_}'}
        params = {'path': folder_name, 'overwrite': 'false'}
        response = requests.put(url=url, headers=headers, params=params)
        print(response)

        folder_creation('Photos')

    def upload_social_network(self, file_name, link):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': f'Photos/photo_1','url':'https://sun9-35.userapi.com/c9591/u00001/136592355/m_672c7bad.jpg'}
        self.headers = {"Accept": "application/json","Authorization": f'OAuth {TOKEN_}'}
        response = requests.post(url=url, params=params, headers=self.headers)
        if response.status_code != 202:
            print(f'Ошибка на сервере. Код ошибки: {response.status_code}')
        else:
            print(response)







            # def upload_file(self, path, url):
            #     #получение URL для загрузки
            #     url = "https://cloud-api.yandex.net/v1/disk/resources/upload?path=https://disk.yandex.ru/client/disk/Photos&overwrite=false&fields=name"
            #     headers = {'Authorization': f'OAuth {TOKEN_}'}
            #     params = {'path': 'file', 'overwrite': 'false', 'fields': 'name'}
            #     response = requests.get(url=url, headers=headers, params=params)
            #     print(response)
            #
            #     #Загрузка файла на полученный URL
            #     for url in urls_list:
            #         url = "https://uploader1d.dst.yandex.net:443/upload-target/20240424T101447.217.utd.52csloukwvq67nab1yc84a3xw-k1d.6625"
            #         response = requests.put(url=url, headers=headers, params=params)
            #         print(response)
