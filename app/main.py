"""Webserver starting point"""
import logging
from os import path
from motor.motor_asyncio import AsyncIOMotorClient
import uvicorn
from fastapi import FastAPI
from app.settings import settings
from app.routers import blogposts

# setup loggers
log_file_path = path.join(path.dirname(path.abspath(__file__)), "logging.conf")
logging.config.fileConfig(log_file_path, disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)

app = FastAPI(docs_url="/docs" if settings.ENVIRONMENT == "staging" else None)


@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(settings.DB_URL)
    # use 'blogposts' collection
    app.mongodb = app.mongodb_client["exampledb"]


app.include_router(blogposts.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()


if __name__ == "__main__":
    uvicorn.run(
        app,
        port=settings.PORT,
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
    )
