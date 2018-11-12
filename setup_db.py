from sqlalchemy_utils import database_exists, create_database, drop_database

import db
from requests_record import Base


engine = db.engine

# if database_exists(engine.url):
#     drop_database(engine.url)

if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)
