from contextlib import contextmanager
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

from db import DB
import sanitizers


app = Flask(__name__)
api = Api(app)

db = DB()

@contextmanager
def sanitizer_scope():
    try:
        yield
    except ValueError as err:
        abort(400, message=str(err))


class GrabAndSave(Resource):
    def post(self):
        return {'hello': 'world'}


class Last(Resource):
    def get(self):
        return db.get_last_requests(number=1, currency=None)


class LastCurrency(Resource):
    def get(self, currency):
        with sanitizer_scope():
            currency = sanitizers.currency(currency)
        return db.get_last_requests(number=1, currency=currency)


class LastN(Resource):
    def get(self, number):
        with sanitizer_scope():
            number = sanitizers.number(number)
        return db.get_last_requests(number, currency=None)


class LastNCurrency(Resource):
    def get(self, number, currency):
        with sanitizer_scope():
            number = sanitizers.number(number)
            currency = sanitizers.currency(currency)
        return db.get_last_requests(number, currency)


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