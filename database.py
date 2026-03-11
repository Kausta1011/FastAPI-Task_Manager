from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

db_url = os.getenv("DATABASE_URL")

engine = create_engine(db_url) 

#Connects Python to Postgres. 
#engine is the core connection interface between SQLAlchemy and PostgreSQL.

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

# A session represents a conversation with #the database.
#Every request should have its own session
# sessionmaker → factory
# session() → actual session
Base = declarative_base()