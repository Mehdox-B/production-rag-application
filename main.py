from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
def welcome():
    return {
        "id":1,
        "message":"Hello mehdox in production rag project"
    }