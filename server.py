#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 heyhx, Inc. All Rights Reserved
#
# @Version : 1.0
# @Author  : snaketao
# @Time    : 2021-10-23 15:32
# @FileName: am_goods_info.py
# @Desc    :
import json
import sys
import re
import time
import es_appbk
import web
import ai_code
#pip install web.py

urls = (
    '/hello', 'hello',
    '/search','search',#搜索
    '/code', 'code',  # 搜索
)

'''
测试
'''
class hello:
    def GET(self):
        web.header('Access-Control-Allow-Origin','*')
        web.header('Content-Type','text/json; charset=utf-8', unique=True)
        web.header('Access-Control-Allow-Credentials', 'true')

        return "hello"

'''
代码搜索
'''
class search:
    def GET(self):
        web.header('Access-Control-Allow-Origin','*')
        web.header('Content-Type','text/json; charset=utf-8', unique=True)
        web.header('Access-Control-Allow-Credentials', 'true')
        param = web.input(word="NFT", start="0", limit="10")
        word = param.word
        start = int(param.start)
        limit = int(param.limit)

        num, result= es_appbk.search_es(word, start, limit)
        final_result = {
            "status":0,
            "msg":"success",
            "num":num,
            "results":result
        }
        return json.dumps(final_result)

'''
生成代码
'''
class code:
    def GET(self):
        web.header('Access-Control-Allow-Origin','*')
        web.header('Content-Type','text/json; charset=utf-8', unique=True)
        web.header('Access-Control-Allow-Credentials', 'true')
        param = web.input(name="Wow", code_type="token")
        name = param.name #合约名称
        code_type = param.code_type #行业类型，token，nft
        if "token" == code_type:
            flow_code = ai_code.generate_token_contract(name)
        else:
            flow_code = ai_code.generate_nft_contract(name)

        final_result = {
            "status":0,
            "msg":"success",
            "results":[
                {"contract":flow_code}
            ]
        }
        return json.dumps(final_result)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

