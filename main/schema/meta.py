#!/usr/bin/env python3
#-*- coding: utf-8 -*-


from utils import call_engine, call_local_engine
from sqlalchemy import MetaData, Table, Column, String, Boolean, ForeignKey, Integer, BigInteger, text

def db_init():

    engine = call_engine()
    # engine = call_local_engine()

    metadata = MetaData()
    
    users = Table("users", metadata,
        Column("id", String(36), primary_key=True),
        Column("name", String, unique=True, nullable=False),
        Column("email", String, unique=True, nullable=False),
        Column("password ", String, nullable=False),   
        Column("token", String),      # False = 'user' AND True = 'admin'
    )

    pose = Table("pose",metadata,
        Column("id", String(36), primary_key=True),
        Column("title", String, unique=True, nullable=False),
        Column("images", String, unique=True, nullable=False),
        Column("description", String, nullable=False), 
        )

    metadata.create_all(engine, checkfirst=True)

    return engine, metadata

## ALREADY CALLED
engine, meta = db_init()