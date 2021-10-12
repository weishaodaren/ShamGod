import requests
import json

def main():
    resp = requests.get('ttp://api.tianapi.com/txapi/duilian/index?key=95c32b6c7c8c24e84f6c3bd032b58997')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])

if __name__ == '__main__':
    main()