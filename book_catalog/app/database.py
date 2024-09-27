from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://bookcatalog_8jg7_user:kgw1X95XC0P96fdmzwAOWU112YNP9w6l@dpg-crjageu8ii6s73fe2na0-a.oregon-postgres.render.com/bookcatalog_8jg7" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
