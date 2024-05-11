import webbrowser
from urllib.parse import quote
import pyautogui
import time


with open('phones.txt', 'r') as phones_file:
    phones_and_names_list = phones_file.readlines()

sceen_wight, screen_height = pyautogui.size()

for row in phones_and_names_list:
    row_list = row.split(',')
    phone = row_list[0]
    name = row_list[0]

    message = f'Здравствуйте {name}! У нас началась распродажа! Скидки до -30%'
    encooded_message = quote(message.encode('utf-8'))

    webbrowser.open(f'https://web.whatsapp.com/send?phone={phone}&text={encooded_message}')
    time.sleep(15)

    pyautogui.click(sceen_wight/2, screen_height/2)
    pyautogui.press('enter')
    time.sleep(2)

    pyautogui.hotkey('cntl','w')

