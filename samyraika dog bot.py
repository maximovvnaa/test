import json
import requests
BOT_TOKEN = '7049383669:AAEawEhcyEjZO62dmlAUrP5u7dbWD4Bmfvc'
get_update = f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates'
dog = f'http://random.dog/woof.json'
send_photo = f'https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto'

params = {
    'offset': 0
}

response = requests.get(get_update, params=params).json()['result'][-1]
dog1 = requests.get(dog).json()
data = {
    'chat_id': response['message']['chat']['id'],
    'photo': dog1['url']
}
response = requests.get(send_photo, data=data)
response = requests.get('http://random.dog/woof.json')