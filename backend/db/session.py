from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from typing import Generator

''' postgresql database '''
SQLALCHEMY_DATABASE_URI = settings.SQLALCHEMY_DATABASE_URL
print("Database URI: {}".format(SQLALCHEMY_DATABASE_URI))

engine = create_engine(SQLALCHEMY_DATABASE_URI)

# ''' sqlite database '''
# SQLALCHEMY_DATABASE_URL = "sqlite:///" + os.path.join(os.path.dirname(__file__), "sql_app.db")
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SESSIONLOCAL = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    try:
        db = SESSIONLOCAL()
        yield db
    finally:
        db.close()