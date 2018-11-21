import time
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy import exc

import db
from requests_record import Base


def setup(tries=0):
    max_tries = 20
    wait = 2

    try:
        engine = db.engine
        # if database_exists(engine.url):
        #     drop_database(engine.url)
        if not database_exists(engine.url):
            create_database(engine.url)
        Base.metadata.create_all(engine)
    except exc.SQLAlchemyError as err:
        if tries < max_tries:
            time.sleep(wait)
            setup(tries + 1)
        else:
            print(' ### ! ### setup_db failed ({})'.format(tries))
            raise err

    print(' ### ! ### setup_db successful ({})'.format(tries))


if __name__ == '__main__':
    setup()
