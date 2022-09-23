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
    status = Column(String)
    name = Column(String)
    target = Column(String)
    description = Column(String)
    progress = Column(String)
    adddate = Column(DateTime, default=datetime.datetime.utcnow)
    deadline = Column(DateTime)
    lastedit_user = Column(String)
    lastedit_time = Column(DateTime)
    manager = Column(String)
    customerManager = Column(String)
    customerManager_contect = Column(String)

class InsertJob(Base):
    __tablename__ = 'insertjob'
    # Input of Json
    job_id=Column(String,primary_key=True)
    job_type = Column(String)
    job_name = Column(String)
    EndUser = Column(String)
    location = Column(String)
    target = Column(String)
    description = Column(String)
    deadLine = Column(String)
    manager = Column(String)
    customer_manger = Column(String)
    customerManager_contect = Column(String)
    #Db Input
    progress = Column(Integer,default=0)
    add_date = Column(DateTime, default=datetime.datetime.utcnow)
    lastedit_user = Column(String)
    lastedit_time = Column(DateTime)
    status = Column(String)
    
    
    
class Auth(Base):
    __tablename__ ="auth"
    id = Column(Integer,primary_key=True, autoincrement=True)
    nickname = Column(String,unique=True)
    password = Column(String)


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine,autocommit=False,autoflush=False)
session = Session()

#Insert Job
def insert_job(JobID,JobType,Status,Name,EndUser,Location,Target):
    query = InsertJob(job_id=JobID,job_type=JobType,status=Status,job_name=Name,EndUser=EndUser,location=Location,target=Target)
    session.add(query)
    session.commit()
    session.close()
##Initialize##



