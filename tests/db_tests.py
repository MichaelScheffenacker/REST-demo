import unittest
import random
import string

from db import DB
from setup_db import Request


class RequestClass(unittest.TestCase):

    def test_insert(self):
        db = DB()
        session = db.get_session()

        letter = random.choice(string.ascii_letters.lower())
        currency = 'TST' + letter

        request = Request(
            currency=currency,
            requested_amount=1,
            exchange_rate=0.88,
            calculated_amount_USD=1.136
        )

        try:
            session.add(request)
            last_entry = session.query(Request).all()[-1]
            self.assertEqual(request, last_entry)

            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

