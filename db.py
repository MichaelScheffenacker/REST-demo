from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from requests_record import RequestRecord


# The db password should not be in this file, nor in the project
# at all.

engine = create_engine('mysql://xapo:xxx@localhost/xapo')
Session = sessionmaker(bind=engine)


# contextmanager implemented as suggested by SQLAlchemy documentation:
# https://docs.sqlalchemy.org/en/latest/orm/session_basics.html#when-do-i-construct-a-session-when-do-i-commit-it-and-when-do-i-close-it
@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


# The following two functions use a complete session cycle, because they
# are self contained and separated in time. If those queries should be
# used with other queries in a block, the session_scope has to move
# where this block is executed, and session has to be passed by argument;
# see the SQLAlchemy documentation for further details.

def select_last_requests(number, currency):
    with session_scope() as session:
        if currency:
            criterion = RequestRecord.currency == currency
            entries = session.query(RequestRecord).filter(criterion).all()[-number:]
        else:
            entries = session.query(RequestRecord).all()[-number:]
        result = [entry.fields_as_dict() for entry in entries]
    return result


def insert_request(request_record):
    with session_scope() as session:
        session.add(request_record)
        session.flush()  # flush() required to get the insert id
        result = request_record.fields_as_dict()
    return result
