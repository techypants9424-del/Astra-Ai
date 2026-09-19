from fastapi import FastAPI

app = FastAPI(title="Astra AI")

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Astra AI server is running!"
    }
