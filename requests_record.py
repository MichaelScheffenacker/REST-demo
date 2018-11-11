from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float


Base = declarative_base()


class RequestRecord(Base):
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

    def fields_as_dict(self):
        return {
            'id': self.id,
            'currency': self.currency,
            'requested_amount': self.requested_amount,
            'exchange_rate': self.exchange_rate,
            'calculated_amount_USD': self.calculated_amount_USD
        }