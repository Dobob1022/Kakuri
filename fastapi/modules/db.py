from time import timezone
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import IntegrityError
from sqlalchemy import Column, Integer, String, DateTime, delete, update
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy.sql import func

engine = create_engine('sqlite:///db/db.sqlite3?check_same_thread=False')#, echo=True)

Base = declarative_base()

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine,autocommit=False,autoflush=False)
session = Session()


class Job(Base):
    __tablename__ = 'joblist'
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
    add_date = Column(DateTime(timezone=True), server_default=func.now())
    lastedit_user = Column(String)
    lastedit_time = Column(DateTime)
    status = Column(String)

class InsertJob(Base):
    __tablename__ = 'InsertJobList'
    job_type = Column(String, primary_key=True)
    job_name = Column(String)
    EndUser = Column(String)
    location = Column(String)
    target = Column(String)
    description = Column(String)
    deadLine = Column(String)
    manager = Column(String)
    customer_manger = Column(String)
    customerManager_contect = Column(String)
    
    
class Auth(Base):
    __tablename__ ="auth"
    id = Column(Integer,primary_key=True, autoincrement=True)
    nickname = Column(String,unique=True)
    password = Column(String)


#Create Table
Job.__table__.create(bind=engine, checkfirst=True)
Auth.__table__.create(bind=engine, checkfirst=True)



#Insert Job
def insert_job(JobID,JobType,Status,Name,EndUser,Location,Target,Manager,Description,DeadLine):
    query = Job(job_id=JobID,job_type=JobType,status=Status,job_name=Name,EndUser=EndUser,location=Location,target=Target,description=Description,manager=Manager,deadLine=DeadLine)
    session.add(query)
    session.commit()
    session.close()

def load_jobs():
    raw_db_Data = session.query(Job.job_id,Job.job_name,Job.EndUser,Job.location,Job.target,Job.description,Job.deadLine,Job.manager,Job.customer_manger,Job.customerManager_contect,Job.progress,Job.add_date,Job.lastedit_time,Job.lastedit_user,Job.status).all()
    
    session.close()
    return raw_db_Data

    
# def load_jobs():
#     # try:
#         return = session.query(Job).all()
#     # except IntegrityError as e:
#     #     session.close()
#     #     return {"msg":"Error On DB!"}
#     # except:
#     #     session.close()
#     #     return {"msg":"DB Connection-ERROR"}

def load_job(JobID):
    # try:
    queried_data = session.query(Job.job_id,Job.job_name,Job.EndUser,Job.location,Job.target,Job.description,Job.deadLine,Job.manager,Job.customer_manger,Job.customerManager_contect,Job.progress,Job.add_date,Job.lastedit_time,Job.lastedit_user,Job.status).filter(Job.job_id==JobID).all()
    # except:
    #     return {"Message":"ERR_ON_DB"}
    # session.close()
    return queried_data
##Initialize##


