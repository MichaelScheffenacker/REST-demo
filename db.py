from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DB:

    def __init__(self):

        # in a more complex situation, this might be implemented as a
        # singleton; on the other hand: in a more complex situation
        # this might be implemented differently anyways.

        self.engine = create_engine('mysql://xapo:xxx@localhost/xapo')
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def get_engine(self):
        return self.engine
