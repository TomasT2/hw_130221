import requests
import re


def parse():
    html = requests.get('https://vk.com/wall-171787766_172', headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150', 'accept': '*/*'})
    if html.status_code == 200:
        match = list(set(re.findall(r"CTF\{\w*?[}]", html.text)))
        print(match, end='\n')
        F = open("CTF скрипт.txt", "w")
        for i in range(len(match)):
            F.write(str(match[i] +  '\n'))
        F.close()
    else:
        print('Error')


parse()