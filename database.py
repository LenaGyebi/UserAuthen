from sqlalchemy import create_engine,Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://postgres:admin@localhost:5432/userauthen', echo=True)

metadata_obj = MetaData()
Base = declarative_base()


user = Table(
    'users', metadata_obj, 

    Column("id", Integer, primary_key=True),
    Column("user_name", String(50), unique=True, nullable=False),
    Column("email", String(50), unique=True, nullable=False),
    Column("password", String(50), unique=True, nullable=False)
    )



for t in metadata_obj.sorted_tables:
    print(t.name)
   

