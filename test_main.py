from unittest import TestCase
from main import Szyfruj, mylist


class TestSzyfruj(TestCase):
    def setUp(self):
        self.szyfruj = Szyfruj()


class TestInit(TestSzyfruj):
    def test_initial_pozyskany_tekst(self):
        self.assertEqual(self.szyfruj.pozyskany_tekst, '')

    def test_initial_pozyskany_tekst2(self):
        self.assertEqual(self.szyfruj.pozyskany_tekst2, '')

    def test_initial_pozyskany_tekst3(self):
        self.assertEqual(self.szyfruj.pozyskany_tekst3, '')



