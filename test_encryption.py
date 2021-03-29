from unittest import TestCase
from encryption import Encrypt, Decrypt
from urllib import parse

class Test(TestCase):

    def setUp(self) -> None:
        self.iv = b"1234567890123456"
        self.key = b"12345678901234567890123456789012"
        self.tradeinfo = "ff91c8aa01379e4de621a44e5f11f72e4d25bdb1a18242db6cef9ef07d80b0165e476fd1d9acaa53170272c82d122961e1a0700a7427cfa1cf90db7f6d6593bb00810249d9e7779bcc1b2ce6fad8f96b11951a00a351a006f45d81af1e733637204574262c146e390c8702eda244a0796f1eb9707c4f79af0f087179a3886aa2"
        self.data = {'MerchantID': 3430112,
                'RespondType': 'JSON',
                'TimeStamp': 1485232229,
                'Version': 1.6,
                'MerchantOrderNo': 'S_1485232229', 'Amt': 40,
                'ItemDesc': 'UnitTest'}
    def test_Encrypt(self):

        self.encrypted = Encrypt(self.data, key=self.key, iv=self.iv)
        self.assertEqual(self.encrypted, self.tradeinfo)

    def test_Decrypt(self):
        self.decrypted = Decrypt(self.encrypted, key=self.key, iv=self.key)
        self.decrypted = dict(parse.parse_qsl(parse.urlsplit(self.decrypted).path))

        self.assertEqual(self.decrypted, self.data)


