import json
from flask import Flask
from flask_restful import Resource, Api, reqparse

from db import DB


app = Flask(__name__)
api = Api(app)

db = DB()


class GrabAndSave(Resource):
    def post(self):
        return {'hello': 'world'}


class Last(Resource):
    def get(self):
        return db.get_last_requests(number=1, currency=None)


class LastCurrency(Resource):
    def get(self, currency):
        return db.get_last_requests(number=1, currency=currency)


class LastN(Resource):
    def get(self, number):
        return db.get_last_requests(number, currency=None)


class LastNCurrency(Resource):
    def get(self, number, currency):
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