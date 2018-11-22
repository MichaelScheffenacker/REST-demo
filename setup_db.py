import time
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy import exc

import db
from requests_record import Base


def setup(tries=0):
    max_sec = 120
    wait_sec = 2
    max_tries = max_sec // wait_sec

    try:
        engine = db.engine
        # if database_exists(engine.url):
        #     drop_database(engine.url)
        if not database_exists(engine.url):
            create_database(engine.url)
        Base.metadata.create_all(engine)
        print(' ### ### setup_db successful (tries:{}, time: {}s)'.format(
            tries,
            tries * wait_sec
        ))
    except exc.SQLAlchemyError as err:
        if tries < max_tries:
            time.sleep(wait_sec)
            setup(tries + 1)
        else:
            print(' ### ### setup_db failed ({}, time: {}s)'.format(
                tries,
                tries * wait_sec
            ))
            raise err


if __name__ == '__main__':
    setup()
