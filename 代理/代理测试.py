import requests
import random


def run(px):
    proxy = px  # 本地代理
    # proxy='username:password@123.58.10.36:8080'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    }
    try:
        response = requests.get('http://httpbin.org/get', proxies=proxies)
        print(response.text)
    except requests.exceptions.ConnectionError as e:
        print('错误:', e.args)


if __name__ == "__main__":
    for line in open("proxy_pool.txt", "r"):
        line = line.strip("\n")
        print(line)
        run(line)
