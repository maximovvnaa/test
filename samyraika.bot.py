import json
import requests

BOT_TOKEN = '7049383669:AAEawEhcyEjZO62dmlAUrP5u7dbWD4Bmfvc'
get_update = f'https://api.telegram.org/bot7049383669:AAEawEhcyEjZO62dmlAUrP5u7dbWD4Bmfvc/getUpdates'
send_message = f'https://api.telegram.org/bot7049383669:AAEawEhcyEjZO62dmlAUrP5u7dbWD4Bmfvc/sendMessage'

params = {
    'offset': 0
}

response = requests.get(get_update, params=params).json()['result'][0]
print(response)
data = {
    'chat_id': response['message']['chat']['id'],
    'text': 'Салам пополам'
}
responce = requests.get(send_message, data=data)
