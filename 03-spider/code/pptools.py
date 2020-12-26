"""
@Time ： 2020/12/17 23:02
@Auth ： 侬&码
@File ：pptool.py
@Description : 代理池工具
"""
import requests


def mogu_proxies_pool(url, count=5):
    """
    获取蘑菇代理
    :param count: 获取的条数
    :param url: 蘑菇代理url
    :return: 代理池
    """
    url = url + f'&count={count}'
    resp = requests.get(url)
    proxies_pool = []
    if resp.status_code == 200:
        json = resp.json()
        if json['code'] == '0':
            for item in json['msg']:
                proxies_pool.append(f"http://{item['ip']}:{item['port']}")
            print('已获取代理池')
        elif json['code'] == '3001':
            print('appkey提取频繁，请按照所购买订单规定的频率进行合理提取。如仍未解决，建议检查相关后台进程！')
        elif json['code'] == '3002' or json['code'] == '3005':
            print('请检查订单的有效时间！')
        elif json['code'] == '3006':
            print('请检查订单的剩余数量！')
        elif json['code'] == '3004':
            print('appkey有误！')
        else:
            print('代理有误！')

    else:
        print('代理有误！')

    return proxies_pool


def main():
    """ 调试方法 """
    pass


if __name__ == '__main__':
    main()
