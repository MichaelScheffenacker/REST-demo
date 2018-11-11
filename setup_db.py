from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database, drop_database

from db import DB


db = DB()
engine = db.get_engine()

# if database_exists(engine.url):
#     drop_database(engine.url)

if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()


class Request(Base):
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True)
    currency = Column(String(4), index=True, nullable=False)
    requested_amount = Column(Float(8), nullable=False)
    exchange_rate = Column(Float(8), nullable=False)
    calculated_amount_USD = Column(Float(8), nullable=False)

    def __repr__(self):
        return "<Request(id: {} req: {} {} rate: {} result: {}>".format(
            self.id,
            self.currency,
            self.requested_amount,
            self.exchange_rate,
            self.calculated_amount_USD
        )


Base.metadata.create_all(engine)
