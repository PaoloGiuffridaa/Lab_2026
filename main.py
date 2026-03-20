from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")   #app.<metodoHTTP>(<path>)
def hello_world():
    return "Hello, World!!"
