from datetime import datetime
from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from modules import db
from pydantic import BaseModel
import datetime as dt

#for TEST

import json

app = FastAPI()

#Fastapi CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#JobClass

# class Job(BaseModel):
#     JobId : str
#     stataus : str
#     Name : str
#     target : str
#     Description : str
#     Progress : str
#     AddDate : str
#     DeadLine : str
#     LastEdit : str
#     LastEditTime : str
#     manager : str
#     customerManger : str
#     customerManager_contect : str

class InsertJob(BaseModel):
    JobType : str
    JobName : str
    EndUser : str
    Location : str
    Target : str
    Description : str
    DeadLine : str
    manager : str
    customerManger : str
    customerManager_contect : str

def JsonConvert(query):
    result =[]
    for dataList in query:
            result.append({
                'JobId':dataList[0],
                'Name':dataList[1],
                'EndUser':dataList[2],
                'Loaction':dataList[3],
                'Target':dataList[4],
                'Description':dataList[5],
                'DeadLine':dataList[6],
                'manager':dataList[7],
                'Customer_manager':dataList[8],
                'Customer_manager_contect':dataList[9],
                'Progress':dataList[10],
                'add_date':dataList[11].strftime('%Y-%m-%d %H:%M:%S'),
                'lastedit_time':dataList[12],
                'lastedit_user':dataList[13],
                'status':dataList[14]
            })
    return result


@app.get("/")
def root():
    return{"msg":"test"}

@app.get("/api/job")
def LoadJobs():
    print(db.load_jobs())
    print(json.dumps(JsonConvert(db.load_jobs())))
    return json.dumps(JsonConvert(db.load_jobs()))

@app.get("/api/job/{job_id}")
def read_jobid(job_id):
    print(json.dumps(JsonConvert(db.load_job(job_id))))
    return json.dumps(JsonConvert(db.load_job(job_id)))

# @app.get("/api/job/20220925-N-Kakaobank")
# def read_jobid():
#     result = {
#         "JobId":"20220922_R_KABANK",
#         "status":"active",
#         "Name":"카뱅-상암-RMA작업",
#         "target":"sp-dat-01",
#         "Description":"TESTJOB",
#         "Progress":"40",
#         "AddDate":"2022-09-22",
#         "DeadLine":"2022-09-23",
#         "LastEdit":"Dobob",
#         "LastEditTime":"2022-09-22",
#         "manager":"dobob",
#         "customerManger":"조성본",
#         "customerManager_contect":"010-1111-1111"
#     }
#     return json.dumps(result)


@app.post("/api/job")
def get_body(request:InsertJob):
    print(request)
    status = "Active"
    #job id get
    date = dt.datetime.now().date()
    enduser = request.EndUser
    JobID = str(date).replace("-","")+"-"+"N"+"-"+enduser
    if request.JobType == "New":
        JobID = str(date).replace("-","")+"-"+"N"+"-"+enduser
        db.insert_job(JobID=JobID,JobType=request.JobType,Status=status,Name=request.JobName,EndUser=request.EndUser,Location=request.Location,Target=request.Target,Manager=request.manager,Description=request.manager,DeadLine=request.DeadLine)
        return {"message":"Sucess!"}
    elif request.JobType == "Delivery":
        JobID = str(date).replace("-","")+"-"+"D"+"-"+enduser
        db.insert_job(JobID=JobID,JobType=request.JobType,Status=status,Name=request.JobName,EndUser=request.EndUser,Location=request.Location,Target=request.Target)
        return {"message":"Sucess!"}
    elif request.JobType == "RMA":
        JobID = str(date).replace("-","")+"-"+"R"+"-"+enduser
        db.insert_job(JobID=JobID,JobType=request.JobType,Status=status,Name=request.JobName,EndUser=request.EndUser,Location=request.Location,Target=request.Target)
        return {"message":"Sucess!"}
    else:
        return "fuq"