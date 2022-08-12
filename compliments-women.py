from time import sleep
import requests
from bs4 import BeautifulSoup
import random
from telethon import TelegramClient

api_id = // your id 
api_hash = '//your hash'

compl = []
print('Сбор комплиментов..')

html = requests.get('https://t-loves.narod.ru/komplimenty-devushke.htm')
soup = BeautifulSoup(html.text, 'lxml')


for link in soup.find_all('p'):
    compl.append(link.text)
    
compl.pop()

print(f'Собрано {len(compl)} комплиментов.')
user = input('Введите ID получателя в Телеграм (без @): ')

while True:
    input(f'Нажмите Enter, чтобы отправить рандомный комплимент.')
    randcompl = compl[random.randint(1,len(compl)-1)]
    print()
    print(randcompl)
    
    with TelegramClient('anon', api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(user, randcompl))
        
        
