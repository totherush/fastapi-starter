from fastapi.testclient import TestClient
from mongomock_motor import AsyncMongoMockClient
import pytest
from pymongo.results import InsertOneResult
from bson import ObjectId
from app.main import app
from app.settings import settings


def test_health_check():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_mock_db():
    # This test meant to check if the db mock is working
    app.mongodb = AsyncMongoMockClient()[settings.DB_NAME]
    payload = {"title": "post from test", "content": "dummy content"}
    blogpost_saved: InsertOneResult = await app.mongodb[settings.DB_NAME].insert_one(
        payload
    )
    inserted_id: str = str(blogpost_saved.inserted_id)
    result = await app.mongodb[settings.DB_NAME].find_one(
        {"_id": ObjectId(inserted_id)}
    )
    # compare title of payload with title of saved record
    assert payload["title"] == result["title"]
