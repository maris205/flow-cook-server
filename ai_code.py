import sys
import datetime
import json
import sql_appbk
import time

#生成code
TOKEN_TEMPLATE = "" #token的模板
NFT_TEMPLATE = "" #NFT的模板

def load_template():
    global TOKEN_TEMPLATE
    TOKEN_TEMPLATE = open("ExampleToken.cdc","r").read()
    #print(TOKEN_TEMPLATE)

    global NFT_TEMPLATE
    NFT_TEMPLATE = open("ExampleNFT.cdc", "r").read()


#加载模板
load_template()


#产生token合约
def generate_token_contract(name="Wow"):
    global TOKEN_TEMPLATE
    ori_name = "Example"
    token_contract = TOKEN_TEMPLATE.replace(ori_name, name)
    #print(token_contract)
    return token_contract


#产生NFT合约
def generate_nft_contract(name="Wow"):
    global NFT_TEMPLATE
    ori_name = "Example"
    nft_contract = NFT_TEMPLATE.replace(ori_name, name)
    #print(nft_contract)
    return nft_contract

if __name__=="__main__":
    name = "WowWar"
    #generate_token_contract(name)
    generate_nft_contract(name)


