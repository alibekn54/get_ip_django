import requests
import socket
import urllib.request


#Получаем Ip пользователя.
def get_user_ip():
    r = requests.get('https://ramziv.com/ip').text
    return r


def get_info_by_ip(ip='214.05.05'): # В поля ip поставьте любой известный вам ip. После этого запустите функцию в main
    try:
        responce = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            'Страна' : responce.get('country'),
            'Регион' : responce.get('region'),
            'Город' : responce.get('city'),
            'Оператор связи' : responce.get('isp')
        }

        for a , b in data.items():
            print(f'{a} : {b}')

        print(f'Расположение на карте:\n'f'https://2gis.kz/almaty/search/{responce.get("lat")},{responce.get("lon")}')

    except requests.exceptions.ConnectionError:
        print('С вашим соидинением что-то не так! Пожалуйста проверьте ваше соединение и повторите попытку.')

def main():
    get_info_by_ip()

if __name__ == '__main__':
    main()
