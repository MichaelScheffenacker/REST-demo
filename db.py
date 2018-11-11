from contextlib import contextmanager
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

    # contextmanager implemented as suggested by sqlalchemy documentation:
    # https://docs.sqlalchemy.org/en/latest/orm/session_basics.html#when-do-i-construct-a-session-when-do-i-commit-it-and-when-do-i-close-it
    @contextmanager
    def session_scope(self):
        session = self.Session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def select_last_requests(self, number, currency):
        with self.session_scope() as session:
            if currency:
                criterion = RequestRecord.currency == currency
                entries = session.query(RequestRecord).filter(criterion).all()[-number:]
            else:
                entries = session.query(RequestRecord).all()[-number:]
            result = [entry.fields_as_dict() for entry in entries]
        return result
