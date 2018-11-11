import unittest
import random
import string

from db import DB
from requests_record import RequestRecord


class RequestClass(unittest.TestCase):

    def test_insert(self):

        # this test cases leaves entries in the 'production'
        # database. I an realistic scenario, it should a) point
        # to a testing db, or b) roll back the queries/inputs.
        # todo: run db tests on a separate db

        db = DB()
        session = db.get_session()

        letter = random.choice(string.ascii_letters.lower())
        currency = 'TS' + letter

        request = RequestRecord(
            currency=currency,
            requested_amount=1,
            exchange_rate=0.88,
            calculated_amount_USD=1.136
        )

        try:
            session.add(request)
            last_entry = session.query(RequestRecord).all()[-1]
            self.assertEqual(request, last_entry)

            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

