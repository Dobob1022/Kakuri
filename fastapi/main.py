from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules import db

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
        "manager":"dobob"
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
        "manager":"dobob"
    }
    return json.dumps(result)



@app.post("/api/job")
def InsertJobs():
    return {"msg":"HAHA"}

