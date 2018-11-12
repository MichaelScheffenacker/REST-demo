import unittest

from oer_requests import get_rate
# todo: import functions from oer_request separately


class GetRate(unittest.TestCase):

    # the following three unittest basically test the sanitizer;
    # it is also used in api.py
    # todo: create a separate sanitizer test

    def test_currency_not_a_string(self):
        self.assertRaises(ValueError,  get_rate, 1)

    def test_currency_not_three_characters(self):
        self.assertRaises(ValueError, get_rate, 'XX')
        self.assertRaises(ValueError, get_rate, 'XXXX')

    def test_currency_invalid_character(self):
        self.assertRaises(ValueError, get_rate, 'EU#')
        self.assertRaises(ValueError, get_rate, 'EUä')
        self.assertRaises(ValueError, get_rate, 'EUá')
        self.assertRaises(ValueError, get_rate, 'EU1')
        self.assertRaises(ValueError, get_rate, 'EU文')
        self.assertRaises(ValueError, get_rate, 'EUµ')

    def test_missing_currency(self):
        self.assertRaises(ValueError, get_rate, 'XXX')

    # the following unittest takes a bit long, since it makes
    # two api calls. Therefore it might be deactivated:
    # def test_currency_lower_case(self):
    #     self.assertEqual(get_rate('eur'), get_rate('EUR'))

    def test_one_euro(self):
        self.assertAlmostEqual(0.88, get_rate('EUR'), 2)
