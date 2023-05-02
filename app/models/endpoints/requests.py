"""Collection of the request data models"""
from typing import Optional
from pydantic import BaseModel


class CreateBlogPostRequestModel(BaseModel):
    """Create blogpost request model"""

    title: str
    content: Optional[str]


class GetBlogPostRequestModel(BaseModel):
    """Get blogpost request model"""

    id: str
