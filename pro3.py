# 全量向es中导入flow_code表数据

import sys
from elasticsearch import Elasticsearch
import datetime
import json
import sql_appbk
import time


# 向es插入一条数据,data格式为dict
# 使用时修改es地址，索引名
def insert_es(result):
    es = Elasticsearch(["http://47.242.206.108:9200"])
    for row in result:
        res = es.index(index="flow_code", body=row, request_timeout=30)
    print(res['result'])


# 读取MySQL数据，插入es
# 使用时修改mysql表
def process():
    # 读取MySQL数据的数据表
    sql_com = 'select * from flow_code;'
    result = sql_appbk.mysql_com(sql_com)
    insert_es(result)
    # for row in result:
    #     print(row)
        # 把row插入es



if __name__ == '__main__':
    process()
