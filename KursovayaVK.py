import configparser
import requests
from pprint import pprint
from tqdm import tqdm
import time

from tqdm import tqdm
import time
for i in tqdm(range(10)):
    time.sleep(0.5)

congig = configparser.ConfigParser()
congig.read("settings.ini")
vk_tk = congig["Tokens"]["vk_token"]
user_id = congig["Tokens"]["user_id"]

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
responce = vk_connector.get_photos('1')
photo_info = {}
items = responce['response']['items']
for item in items:
    likes = item['likes']['count']
    sizes = item['sizes']
    name = str(likes)
    url, type = vk_connector.max_size_photo(sizes)
    photo_info[name] = str({'url': url, 'type': type})

#pprint(photo_info)

with open('test_write.txt', "w", encoding = "utf-8") as f:
    for photo in photo_info:
        f.write(photo_info[name])
        f.write(str(photo_info[name][0]) + '\n')
        print("\n".join(map(str, photo_info)), file=f)


class YD:
    def __init__(self, token):
        self.params = {'access_token': token, 'v': version}
        print('создался ЯД')

    def create_folder(self, folder_name):
        requests.put(f'{https://cloud-api.yandex.net/v1/disk/resources?path=%2FMy_photos}?path={path}')
        create_folder('My_photos')

    def upload_file(self, path, url):
        for photo in photo_info:
            upload_file(r'https://cloud-api.yandex.net/v1/disk/resources/upload?path=My_photos%2Fimage.jpg&url=https%3A%2F%2F"url"')


