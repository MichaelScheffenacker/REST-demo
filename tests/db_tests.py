import unittest
import random
import string

import db
from requests_record import RequestRecord


class RequestClass(unittest.TestCase):

    def test_insert_and_select(self):

        # this test cases leaves entries in the 'production'
        # database. In a realistic scenario, it should a) point
        # to a testing db, or b) roll back the queries/inputs.
        # todo: run db tests on a separate db

        letter = random.choice(string.ascii_letters.lower())
        currency = 'TS' + letter

        request = RequestRecord(
            currency=currency,
            requested_amount=1,
            exchange_rate=0.88,
            calculated_amount_USD=1.136
        )

        db.insert_request(request)
        result = db.select_last_requests(number=1, currency=currency)
        self.assertEqual(currency, result[0]['currency'])
