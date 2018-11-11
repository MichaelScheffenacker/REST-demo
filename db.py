from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from requests_record import RequestRecord


class DB:

    def __init__(self):

        # in a more complex situation, this might be implemented as a
        # singleton; on the other hand: in a more complex situation
        # this might be implemented differently anyways.
        # The db password should not be in this file, nor in the project
        # at all.

        self.engine = create_engine('mysql://xapo:xxx@localhost/xapo')
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def get_engine(self):
        return self.engine

    def get_last_requests(self, number, currency):
        session = self.Session()
        try:
            if currency:
                filt = RequestRecord.currency == currency
                entries = session.query(RequestRecord).filter(filt).all()[-number:]
            else:
                entries = session.query(RequestRecord).all()[-number:]
            result = [entry.fields_as_dict() for entry in entries]
            if len(result) == 1:
                result = result[0]
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return result
