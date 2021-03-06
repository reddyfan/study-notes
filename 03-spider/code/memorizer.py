"""
@Time ： 2020/12/18 20:34
@Auth ： 侬&码
@File ：memorize.py
@Description : 存储器
"""

import csv
import os





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

        csv_file.writerows(data)


def read_csv(filename, encoding='utf-8'):
    """
    读取csv文件 
    :param filename: 文件名
    :param encoding: 编码
    :return: 读取的文件数据
    """
    if os.path.exists(filename):
        with open(filename, 'r', encoding=encoding) as file:
            reader = csv.reader(file)
            return [item for item in reader]