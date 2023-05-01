"""Module for the stripe customer endpoints"""

import logging
from fastapi import Request, APIRouter
from app.models.endpoints.responses import CreateBlogPostResponseModel
from app.models.endpoints.requests import (
    CreateBlogPostRequestModel,
)
from app.models.db.blogposts import BlogPostModel
from app.repositories.blogpost import BlogPostRepository

logger = logging.getLogger(__name__)
router = APIRouter(
    prefix="/v1/blogposts",
    tags=["blogposts"],
)


@router.post("", response_model=CreateBlogPostResponseModel)
async def create_blogpost(request: Request, payload: CreateBlogPostRequestModel):
    """Creates a blogpost"""
    logger.info("create_blogpost request payload: %s", payload)
    blogpost_repo = BlogPostRepository(request=request)
    blogpost_dict = payload.dict()
    result = await blogpost_repo.create_blogpost(blogpost_dict)
    return result


@router.get("/{blogpost_id}", response_model=BlogPostModel)
async def get_blogpost(blogpost_id: str, request: Request):
    """Gets a blogpost by id"""
    logger.info("get_blogpost by id: %s", blogpost_id)
    blogpost_repo = BlogPostRepository(request=request)
    blogpost_result: BlogPostModel = await blogpost_repo.get_blogpost(blogpost_id)
    return blogpost_result.dict()
