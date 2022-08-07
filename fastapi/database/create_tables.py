import sqlalchemy

from database.config import DATABASE_URL, metadata

def config_db(database_url = DATABASE_URL):
  engine = sqlalchemy.create_engine(database_url)
  metadata.drop_all(engine)
  metadata.create_all(engine)
