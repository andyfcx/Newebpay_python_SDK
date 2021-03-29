from Crypto.Cipher import AES
import urllib.parse
import binascii
import hashlib


# key = b'12345678901234567890123456789012'
# iv = b'1234567890123456'
# data = {'MerchantID': 3430112,
#         'RespondType': 'JSON',
#         'TimeStamp': 1485232229,
#         'Version': 1.6,
#         'MerchantOrderNo': 'S_1485232229', 'Amt': 40,
#         'ItemDesc': 'UnitTest'}


def AES_encrypted_bytes(data: str, key: bytes, iv: bytes) -> bytes:
    cryptor = AES.new(key, AES.MODE_CBC, iv)
    return cryptor.encrypt(str.encode(PKC5padding(data)))


def AES_decryptd_bytes(data:str, key: bytes, iv: bytes) -> bytes:
    cryptor = AES.new(key, AES.MODE_CBC, iv)
    return cryptor.decrypt(data)


def Encrypt(form_data, key: bytes, iv: bytes) -> str:
    if not isinstance(form_data, str):
        form_data = urllib.parse.urlencode(form_data)
    AES_info = AES_encrypted_bytes(form_data, key, iv)
    TradeInfo = str(binascii.hexlify(AES_info), 'ascii')
    return TradeInfo


def PKC5padding(string, blocksize=32):
    pad = blocksize - (len(string) % blocksize)
    string += chr(pad) * pad
    return string


def EncryptSHA256(AES_plus):
    m = hashlib.sha256()
    m.update(AES_plus.encode('ascii'))
    SHA_info = m.digest()
    SHA_encrypted_string = str(binascii.hexlify(SHA_info), 'ascii')
    TradeSHA = SHA_encrypted_string.upper()
    return TradeSHA


def Decrypt(encrypedtext: str, key: bytes, iv: bytes) -> str:
    AES_info = encrypedtext.encode('utf-8')
    AES_info = binascii.unhexlify(AES_info)
    AES_info = AES_decryptd_bytes(AES_info, key, iv).decode("utf-8")
    padding_str = AES_info[-1]
    AES_info = AES_info.strip(padding_str)
    return AES_info
