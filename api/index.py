from fastapi import FastAPI
from mangum import Mangum  # Vercel के लिए ASGI एडॉप्टर

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, Vercel!"}

# Vercel को FastAPI ऐप हैंडल करने के लिए एक ASGI हैंडलर चाहिए
handler = Mangum(app)
