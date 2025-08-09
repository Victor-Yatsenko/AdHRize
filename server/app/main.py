from fastapi import FastAPI
from services import password_generator as pg

pg = pg.PasswordGenerator(length=10)
print(pg.generate())

# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "AdHRize Backend is running"}
