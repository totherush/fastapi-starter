"""Collection of the request data models"""
from typing import Optional
from pydantic import BaseModel


class CreateBlogPostRequestModel(BaseModel):
    """Get foo request model"""

    title: str
    content: Optional[str]


class GetBlogPostRequestModel(BaseModel):
    """Get foo request model"""

    id: str
