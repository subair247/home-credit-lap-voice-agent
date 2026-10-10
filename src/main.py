from fastapi import FastAPI
from src.routes.webhook import router as webhook_router
from src.config import Config

app = FastAPI(title="Home Credit LAP Voice Agent API", version="1.0.0")

app.include_router(webhook_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Home Credit LAP Voice Agent Backend is running successfully!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=Config.PORT, reload=Config.DEBUG)