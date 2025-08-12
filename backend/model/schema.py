from sqlalchemy import create_engine,Column,INTEGER,String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL="postgresql://aymen:aymen@localhost/aymen"

engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
base=declarative_base()



class book(base):
    __tablename__="books"

    id=Column(INTEGER,primary_key=True,index=True)
    title=Column(String,index=True)
    file_path=Column(String,index=True)
    created_at=Column(DateTime,default=DateTime.utcnow)

base.metadata.create_all(bind=engine)