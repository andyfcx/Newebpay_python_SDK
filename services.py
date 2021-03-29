import json, os, uuid, time
from encryption import *

def generateEncryptedData(MerchantOrderNo='MI00000000', email='andyhuang@mirrormedia.mg', charge_type='CREDIT'):
    MerchantID = os.getenv('MerchantID')
    key = bytes(os.getenv('key'),'utf-8')
    iv = bytes(os.getenv('iv'),'utf-8')

    # Setting order parameters
    order_params = {
        'MerchantID': MerchantID,
        'RespondType': 'JSON',
        'TimeStamp': f'{int(time.time())}',
        'Version': '1.6',
        'P3D':1,
        'LangType': 'zh-tw',
        'MerchantOrderNo': MerchantOrderNo,
        'Amt':  50,
        'ItemDesc': "紙本雜誌訂閱",
        'PeriodAmt': '1',
        'PeriodType':'M',
        'PeriodPoint':'30',
        'PeriodStartType':'1',
        'PeriodTimes':'1',
        'PeriodMemo':"TEST",
        'PayerEmail': email,
        'TradeLimit': 0, # 0 for no limit, use any int number 60~900 seconds as trade time limit 
        'NotifyURL': "https://mirror-bill.insowe.com/zh-Hant/api/bill/pay_result", # 接收交易資訊
        'Email':email, # 交易完成通知付款人
        'EmailModify': 0,
        'LoginType': 0,
        'CREDITAGREEMENT': 1,
        'OrderComment': 'Simple test',
        f'{charge_type}': 1,
        'TokenTerm':email
        # 'InstFlag': 0, # 分期功能
    }
    
    # AES encode 
    TradeInfo = Encrypt(order_params, key, iv)

    # SHA256 encode
    AES_plus = f'HashKey={key}&{TradeInfo}&HashIV={iv}'
    TradeSha = EncryptSHA256(AES_plus)

    # Combine all needed parameters
    data = {
        'MerchantID':MerchantID,
        'TradeInfo':TradeInfo,
        'TradeSha':TradeSha,
        'Version':'1.6'
    }

    return data