from sqlalchemy import create_engine, Column, Integer, String, DateTime, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://postgres:admin@localhost:5432/userauthen', echo=True)

metadata_obj = MetaData()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users', metadata_obj, 

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), unique=True, nullable=False)


for t in metadata_obj.sorted_tables:
    print(t.name)
   

