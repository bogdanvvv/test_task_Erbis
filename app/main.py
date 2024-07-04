from fastapi import FastAPI
from routers import router
import uvicorn

app = FastAPI(docs_url="/api/docs")

app.include_router(router, prefix='/api/v1')

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8080)