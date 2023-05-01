"""Module which contains the reusable DB queries"""
from fastapi import Request
from bson import ObjectId
from pymongo.results import InsertOneResult
from app.models.endpoints.responses import CreateBlogPostResponseModel
from app.models.db.blogposts import BlogPostModel


class BlogPostRepository:
    def __init__(self, request: Request):
        self.collection = request.app.mongodb["blogposts"]

    async def create_blogpost(self, post_dict) -> CreateBlogPostResponseModel:
        """Saves a blogpost to db"""
        result: InsertOneResult = await self.collection.insert_one(post_dict)
        inserted_id: ObjectId = result.inserted_id
        return CreateBlogPostResponseModel(id=str(inserted_id))

    async def get_blogpost(self, blogpost_id: str) -> BlogPostModel:
        """Retrieves a blogpost from db"""
        blogpost = await self.collection.find_one({"_id": ObjectId(blogpost_id)})
        blogpost_model = BlogPostModel(**blogpost)
        return blogpost_model

    def get_blogposts(self):
        """Retrieves all blogposts from db"""
        posts = self.collection.find()
        return posts
