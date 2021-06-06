from unittest import TestCase
from main import Beaufort


class TestBeaufort(TestCase):
    def setUp(self):
        self.beaufort = Beaufort()


class TestInit(TestBeaufort):
    def test_initial_key(self):
        self.assertEqual(self.beaufort.key, 'C')


class TestSzyfruj(TestBeaufort):
    def test_szyfruj_lub_deszyfruj(self):
        test = self.beaufort.szyfruj_lub_deszyfruj('test')
        self.assertEqual(test,'JYKJ')

    def test_szyfruj_lub_deszyfruj2(self):
        test = self.beaufort.szyfruj_lub_deszyfruj('test')
        test2 = self.beaufort.szyfruj_lub_deszyfruj(test)
        self.assertEqual(self.beaufort.szyfruj_lub_deszyfruj(test2),test)

