from contextlib import contextmanager
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

import db
import sanitizers
from requests_record import RequestRecord
from oer_requests import get_rate


app = Flask(__name__)
api = Api(app)


@contextmanager
def sanitizer_scope():
    try:
        yield
    except ValueError as err:
        abort(400, message=str(err))


parser = reqparse.RequestParser()
parser.add_argument(
    'amount',
    type=float,
    help="'amount' has to be a float that represents the amount in the given currency"
)
parser.add_argument(
    'currency',
    type=str,
    help="'currency' has to be a string with exactly three letters [A-Z] e.g. EUR"
)


class GrabAndSave(Resource):
    def post(self):
        args = parser.parse_args(strict=True)
        with sanitizer_scope():
            amount = sanitizers.amount(args['amount'])
            currency = sanitizers.currency(args['currency'])
            exchange_rate = get_rate(currency)

        calculated_amount = amount / exchange_rate

        request = RequestRecord(
            currency=currency,
            requested_amount=amount,
            exchange_rate=exchange_rate,
            calculated_amount_USD=calculated_amount
        )

        db.insert_request(request)


class Last(Resource):
    def get(self):
        return db.select_last_requests(number=1, currency=None)


class LastCurrency(Resource):
    def get(self, currency):
        with sanitizer_scope():
            currency = sanitizers.currency(currency)
        return db.select_last_requests(number=1, currency=currency)


class LastN(Resource):
    def get(self, number):
        with sanitizer_scope():
            number = sanitizers.number(number)
        return db.select_last_requests(number, currency=None)


class LastNCurrency(Resource):
    def get(self, number, currency):
        with sanitizer_scope():
            number = sanitizers.number(number)
            currency = sanitizers.currency(currency)
        return db.select_last_requests(number, currency)


api.add_resource(GrabAndSave, '/grab_and_save')
api.add_resource(Last, '/last')
api.add_resource(LastCurrency, '/last/<string:currency>')
api.add_resource(LastN, '/last/<int:number>')
api.add_resource(
    LastNCurrency,
    '/last/<int:number>/<string:currency>',
    '/last/<string:currency>/<int:number>'
)

if __name__ == '__main__':
    app.run(debug=True)