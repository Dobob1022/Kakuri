from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import IntegrityError
from sqlalchemy import Column, Integer, String, DateTime, delete, update
import datetime

engine = create_engine('sqlite:///db/db.sqlite3?check_same_thread=False')#, echo=True)

Base = declarative_base()

class Job(Base):
    __tablename__ = 'joblist'
    job_id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    description = Column(String)
    progress = Column(String)
    adddate = Column(DateTime, default=datetime.datetime.utcnow)
    deadline = Column(DateTime)
    lastedit_time = Column(DateTime)
    lastedit_user = Column(String)
    manager = Column(String)

    
class Auth(Base):
    __tablename__ ="auth"
    id = Column(Integer,primary_key=True, autoincrement=True)
    nickname = Column(String,unique=True)
    password = Column(String)


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine,autocommit=False,autoflush=False)
session = Session()

##Initialize##



