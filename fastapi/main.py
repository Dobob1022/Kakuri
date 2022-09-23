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
    EndUser : str
    JobName : str
    Location : str
    Target : str
    Description : str
    DeadLine : str
    manager : str
    customerManger : str
    customerManager_contect : str


testjob = [{
        "JobId":"20220922_R_KABANK",
        "status":"active",
        "Name":"카뱅-상암-RMA작업",
        "target":"sp-dat-01",
        "Description":"TESTJOB",
        "Progress":"40",
        "AddDate":"2022-09-22",
        "DeadLine":"2022-09-23",
        "LastEdit":"Dobob",
        "LastEditTime":"2022-09-22",
        "manager":"dobob",
        "customerManger":"조성본",
        "customerManager_contect":"010-1111-1111"
    },
    {
        "JobId":"20220922_N_TOSS",
        "status":"inactive",
        "Name":"토스모니터20대납품",
        "target":"sp-dat-01",
        "Description":"TESTJOB",
        "Progress":"100",
        "AddDate":"2022-09-22",
        "DeadLine":"2022-09-23",
        "LastEdit":"Dobob",
        "LastEditTime":"2022-09-22",
        "manager":"dobob"
    }
    ]

@app.get("/")
def root():
    return{"msg":"test"}

@app.get("/api/job")
def LoadJobs():
    return json.dumps(testjob)

# @app.get("/api/job/{job_id}")
# def read_jobid(job_id):
#     return {"jobid":job_id}

@app.get("/api/job/20220922_R_KABANK")
def read_jobid():
    result = {
        "JobId":"20220922_R_KABANK",
        "status":"active",
        "Name":"카뱅-상암-RMA작업",
        "target":"sp-dat-01",
        "Description":"TESTJOB",
        "Progress":"40",
        "AddDate":"2022-09-22",
        "DeadLine":"2022-09-23",
        "LastEdit":"Dobob",
        "LastEditTime":"2022-09-22",
        "manager":"dobob",
        "customerManger":"조성본",
        "customerManager_contect":"010-1111-1111"
    }
    return json.dumps(result)


@app.post("/api/job")
def get_body(request:InsertJob):
    print(request)
    status = "Active"
    #job id get
    date = dt.datetime.now().date()
    enduser = request.EndUser
    if request.JobType == "New":
        JobID = str(date)+"-"+"N"+"-"+enduser
        db.insert_job(JobID=JobID,JobType=request.JobType,Status=status,Name=request.JobName,EndUser=request.EndUser,Location=request.Location,Target=request.Target)
    elif request.JobType == "Delivery":
        JobID = str(date)+"-"+"D"+"-"+enduser
    elif request.JobType == "RMA":
        JobID = str(date)+"-"+"R"+"-"+enduser
    else:
        return "fuq"



    return request