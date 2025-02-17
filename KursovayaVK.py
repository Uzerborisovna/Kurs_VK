import configparser
import requests
from pprint import pprint
from tqdm import tqdm
import time

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
         response = response.json()
         return response


vk_connector = VK(vk_tk)
photos_dict = vk_connector.get_photos(user_id)

items_response = photos_dict["response"]["items"]
sizes = [свой_словарь['sizes'] for свой_словарь in items_response if 'sizes' in свой_словарь]
#pprint(sizes)
types = [свой_словарь['type'] for свой_словарь in items_response if 'type' in свой_словарь]
pprint(types)

for type in types:
    if type in {"w", "z", "y", "r"}:
        pprint(types)


# def max_size_photo(self, sizes):
#     types = ["w", "z", "y", "r", "q", "p", "o", "x", "m", "s"]
#     for type in types:
#         for size in sizes:
#             if size["type"] == type:
#                 return size["url"], type
#     max_photo_url, size = self.max_size_photo(item["sizes"])
#     pprint(max_photo_url, size)

# max_photos = {}
# for photo in photos_dict:
#     photos_list = photos_dict["response"]["items"][2]["sizes"]
#     for photos in photos_list:
#         if type == "w" or type == "x" or type == "y" or type == "z":
#             pprint(photos.get('url', None))

# class YD:
#     def __init__(self, token):
#         self.params = {'access_token': token, 'v': version}
#         print('создался ЯД')
#
#     def create_folder(self, folder_name):
#         pass
#
#     def upload_file(self, path, url):
#         pass

    # params.update(self.params)
    # response = requests.get(url, params=params)
    # return response.json()

# https://cloud-api.yandex.net/v1/disk/resources/upload
#  url=<ссылка на скачиваемый файл>
#  path=<путь к папке, в которую нужно скачать файл>
#  [fields=<свойства, которые нужно включить в ответ>]
#  [disable_redirects=<признак запрета редиректов>]

# from tqdm import tqdm
# import time
# for i in tqdm(range(10)):
#     time.sleep(0.5)  # Имитация работы