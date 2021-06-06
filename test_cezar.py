from unittest import TestCase
from main import Cezar


class TestCezar(TestCase):
    def setUp(self):
        self.cezar = Cezar()


class TestInit(TestCezar):
    def test_initial_KLUCZ(self):
        self.assertEqual(self.cezar.KLUCZ, 3)


class TestSzyfruj(TestCezar):
    def test_szyfruj(self):
        test = self.cezar.szyfruj_cezar('test')
        self.assertEqual(test,'whvw')

    def test_deszyfruj2(self):
        test = self.cezar.deszyfruj_cezar('whvw')
        self.assertEqual(test,'test')
