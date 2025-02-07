import configparser
import requests

from tqdm import tqdm
import time

congig = configparser.ConfigParser()
congig.read("settings.ini")
vk_tk = congig["Tokens"]["vk_token"]
user_id = congig["Tokens"]["user_id"]
#print(len(vk_tk))

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


vk_connector = VK(vk_tk)
print(vk_connector.get_photos(user_id))





# from tqdm import tqdm
# import time
# for i in tqdm(range(10)):
#     time.sleep(0.5)  # Имитация работы