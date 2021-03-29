import os
import requests
from services import generateEncryptedData

test_url = "https://ccore.newebpay.com/MPG/mpg_gateway"

data = generateEncryptedData()

MerchantID = os.getenv('MerchantID')
session = requests.Session()
r = session.post(test_url, data={"MerchantID": MerchantID,
                                  "TradeInfo": data['TradeInfo'],
                                 "TradeSha": data['TradeSha'],
                                 "Version":"1.6"
                                  }) #MPG03007



print(r.text)