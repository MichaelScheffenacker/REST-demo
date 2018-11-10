import unittest

import oer_requests as oerr


class GetRate(unittest.TestCase):

    def test_currency_not_a_string(self):
        self.assertRaises(ValueError,  oerr.get_rate, 1)

    def test_currency_not_three_characters(self):
        self.assertRaises(ValueError, oerr.get_rate, 'XX')
        self.assertRaises(ValueError, oerr.get_rate, 'XXXX')

    def test_currency_invalid_character(self):
        self.assertRaises(ValueError, oerr.get_rate, 'EU#')
        self.assertRaises(ValueError, oerr.get_rate, 'EUä')
        self.assertRaises(ValueError, oerr.get_rate, 'EUá')
        self.assertRaises(ValueError, oerr.get_rate, 'EU1')
        self.assertRaises(ValueError, oerr.get_rate, 'EU文')
        self.assertRaises(ValueError, oerr.get_rate, 'EUµ')

    # def test_currency_lower_case(self):
    #     self.assertEqual(oerr.get_rate('eur'), oerr.get_rate('EUR'))

    def test_one_euro(self):
        self.assertAlmostEqual(0.88, oerr.get_rate('EUR'), 2)


