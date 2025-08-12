from fastapi import FastAPI ,UploadFile, File
from fastapi.middleware import CORSMiddleware
from pydantic import BaseModel
import os 
from datetime import datetime
import uuid
from sqlalchemy import create_engine,Column,INTEGER,String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from model.schema import SessionLocal, base,book
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def uploadbook(file:UploadFile=File(...)):

