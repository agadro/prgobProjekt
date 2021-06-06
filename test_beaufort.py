from unittest import TestCase
from main import szyfruj_lub_deszyfruj

class Test(TestCase):


    def test_szyfruj_lub_deszyfruj(self):
        self.assertEqual('test',szyfruj_lub_deszyfruj('jykj'))
