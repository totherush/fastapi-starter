import json
from mongomock_motor import AsyncMongoMockClient
import pytest
from httpx import AsyncClient, Response
from app.main import app
from app.settings import settings
from app.utils.httpx_wrapper import HttpxWrapper
from app.models.endpoints.responses import CreateBlogPostResponseModel
from app.models.db.blogposts import BlogPostModel


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "title,content",
    [
        (
            "very first test post",
            "lorem ipsum dummy content",
        ),
        (
            "second test post",
            "lorem ipsum dummy content",
        ),
        (
            "third test post",
            "lorem ipsum dummy content",
        ),
    ],
)
async def test_create_blogpost(title, content):
    """These tests will:
    - Create a blogpost by using the POST /v1/blogposts endpoint
    - Verifies that the record is in the mocked db
    - Deletes the created blogpost entry again
    - Des
    """
    # Mock the db
    app.mongodb = AsyncMongoMockClient()[settings.DB_NAME]
    payload = {"title": title, "content": content}
    json_data = json.loads(json.dumps(payload))

    async_client = AsyncClient(app=app, base_url="http://example")

    # create blogpost via endpoint
    blogpost_created_response: Response = await async_client.post(
        url="/v1/blogposts", json=json_data
    )
    blogpost_created = CreateBlogPostResponseModel(**blogpost_created_response.json())

    # get a blogpost via endpooint
    blogbpost_fetched_response: Response = await async_client.get(
        url=f"/v1/blogposts/{blogpost_created.id}"
    )
    blogpost_fetched: BlogPostModel = BlogPostModel(**blogbpost_fetched_response.json())

    assert blogpost_fetched.title == title
    assert blogpost_fetched.content == content

    # Mock: make some other http calls
    httpx_wrapper = HttpxWrapper()
    dummy_response: Response = await httpx_wrapper.request(
        method="get", url="https://jsonplaceholder.typicode.com/todos/1"
    )
    dummy_data = dummy_response.json()
    assert bool(dummy_data.get("userId", False))
