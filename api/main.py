import os
import uvicorn

from fastapi import FastAPI

from deliveries.routes import delivery_router

app = FastAPI()

app.include_router(delivery_router, tags=["delivery"])


@app.get("/api")
async def root():
    return {"message": "Hello, FastAPI!"}


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))