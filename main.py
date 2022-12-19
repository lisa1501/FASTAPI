import imp
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_posts():
    return {"data": "This is my first post."}
@app.get("/")
def root():
    return {"message": "Hello World!"}

