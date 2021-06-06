from unittest import TestCase
from main import Base64


class TestBase64(TestCase):
    def setUp(self):
        self.base64 = Base64()


class TestSzyfruj(TestBase64):
    def test_szyfruj(self):
        test = self.base64.szyfruj_base64('test')
        self.assertEqual(test,'dGVzdA==')


    def test_deszyfruj2(self):
        test = self.base64.deszyfruj_base64('dGVzdA==')
        self.assertEqual(test,'test')
