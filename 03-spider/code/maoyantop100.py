"""
@Time ： 2020/12/18 10:54
@Auth ： 侬&码
@File ：maoyantop100.py
@Description : 爬取猫眼top100
"""
import csv
import json
import os
import random
import re
import time

import requests

# top正则表达式
TOP_RE_STR = r'<dd>[\s\S]*?board-index-\d+">(\d+)</i>[\s\S]*?' \
             r'data-src="([\s\S]*?)"[\s\S]*?' \
             r'movieId:\d+}">(.+?)</a>[\s\S]*?' \
             r'主演：([\s\S]*?)\n[\s\S]*?' \
             r'上映时间：([\s\S]*?)</p>[\s\S]*?' \
             r'integer">(\d\.)[\s\S]*?' \
             r'fraction">(\d)'

movie_cols = (
    'rank', 'image_url', 'name',
    'star', 'release_data', 'country', 'score'
)


def get_page(url, proxies, offset=10):
    """
    获取页面
    :param url: 网址
    :param proxies: 代理
    :param offset: 偏移量
    :return: html页面
    """
    url += f'?offset={offset}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36'
    }
    resp = requests.get(url, proxies=proxies, headers=headers)
    page = resp.text
    if resp.status_code == 200 and page:
        return page

    return None


def get_data_re(page):
    """
    用正则获取数据
    :param page: 页面内容
    :return: 已处理的数据（列表）
    """
    top_re = re.compile(TOP_RE_STR)
    top_list = top_re.findall(page)
    if top_list:
        top = []
        for i in top_list:
            i = list(i)
            if '(' in i[-3]:
                i[-3], country = i[-3].split('(')
                i.insert(-2, country[:-1])
            else:
                i.insert(-2, '')

            # 评分设置
            score = i[-2] + i[-1]
            i.insert(-2, score)
            i = i[:-2]
            top.append(i)

    else:
        print('请检查正则或页面是否正确')
        print(page)
    return top


def to_dict(columns, data):
    """
    将字段和数据组成字典
    :param columns: 字段
    :param data: 序列数据
    :return: 字典
    """
    return [dict(zip(columns, item)) for item in data]


def to_csv(filename, data, columns=None, encoding='utf-8'):
    """
    将数据存储为csv文件，如有同名文件即是追加
    :param filename: 文件名
    :param data: 数据集
    :param columns: 字段
    :param encoding: 编码
    :return:
    """
    flag = os.path.exists(filename)
    with open(filename, 'a', encoding=encoding, newline='') as file:
        csv_file = csv.writer(file)
        if (not flag) and columns:
            csv_file.writerow(columns)

        for item in data:
            csv_file.writerow(item)


def to_txt_json(filename, data, columns=None, encoding='utf-8'):
    """
    将数据存储为txt文件，如有同名文件即是追加
    :param filename: 文件名
    :param data: 数据集
    :param columns: 字段
    :param encoding: 编码
    :return:
    """
    flag = os.path.exists(filename)
    print(flag)
    with open(filename, 'a', encoding=encoding) as file:
        if (not flag) and columns:
            print(columns)
            file.write(json.dumps(columns, ensure_ascii=False) + '\n')
        for item in data:
            file.write(json.dumps(item, ensure_ascii=False) + '\n')

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
        agent_json = resp.json()
        if agent_json['code'] == '0':
            for item in agent_json['msg']:
                proxies_pool.append(f"http://{item['ip']}:{item['port']}")
            print('已获取代理池')
        elif agent_json['code'] == '3001':
            print('appkey提取频繁，请按照所购买订单规定的频率进行合理提取。如仍未解决，建议检查相关后台进程！')
        elif agent_json['code'] == '3002' or agent_json['code'] == '3005':
            print('请检查订单的有效时间！')
        elif agent_json['code'] == '3006':
            print('请检查订单的剩余数量！')
        elif agent_json['code'] == '3004':
            print('appkey有误！')
        else:
            print('代理有误！')

    else:
        print('代理有误！')

    return proxies_pool


def main():
    """ 主方法 """
    url = 'https://maoyan.com/board/4'
    # 代理url
    mogu_url = 'http://piping.mogumiao.com/proxy/api/get_ip_al' \
               '?appKey=b3e67385fc9449aea21aac7c02c1fe73&expiryDate=0' \
               '&format=1&newLine=2'
    pool = mogu_proxies_pool(mogu_url, 5)
    num = 0
    while True:
        for num in range(10):
            print(f'第{num + 1}页开始')
            proxies = {
                'https': random.choice(pool)
            }
            print(proxies['https'])
            page = get_page(url, proxies, num * 10)
            data = get_data_re(page)
            if data:
                for item in data:
                    print(item)
                to_csv('top.csv', data, movie_cols)
                print(f'第{num + 1}页保存成功')
                time.sleep(random.randint(6, 8))
            else:
                print('================爬取失败！未为获取页面===================')
                time.sleep(3)
                break
        else:
            print('================爬取完成！===================')
            break

        print('================爬取结束！===================')


if __name__ == '__main__':
    main()
