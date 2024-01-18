from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = ''


engine = create_engine(URL_DATABASE)

# autocommit=False means that SQLAlchemy will not automatically commit changes to the database.
# autoflush=False means that SQLAlchemy will not automatically flush the session. Flushing is committing the changes to the database.
# bind=engine means that the session will use the engine we set up earlier.

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is the declarative base class from which all mapped classes should inherit.
base = declarative_base()