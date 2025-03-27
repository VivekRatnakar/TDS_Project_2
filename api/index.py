from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # ✅ Check this matches your request path
async def root():
    return {"message": "Hello, world!"}
