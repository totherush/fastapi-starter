"""Collection of the response data models"""
from pydantic import BaseModel


class CreateBlogPostResponseModel(BaseModel):
    """Create blogpost response model"""

    id: str
