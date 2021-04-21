import requests

bot_key ='1526355880:AAGfr5_2SbmPn4nb38Prnj7r88-wQ52wH8o'
chat_id='1109158839'

def send_update(chat_id,msg):
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)

def main():
    send_update(chat_id,"hi")

main()