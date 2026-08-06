from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def message():
    return {"message: Welcome to Atlanta Hawks Revenue Copilot!"}