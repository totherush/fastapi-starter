"""httpx calls wrapper"""
import logging
from typing import Union
from fastapi import HTTPException
import httpx


class HttpxWrapper:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def raise_error(self, error_message: str):
        raise HTTPException(
            status_code=500,
            detail=error_message,
        )

    async def request(
        self, method: str, url: str, body: Union[None, dict] = None, raise_error=True
    ):
        if method == "get":
            async with httpx.AsyncClient() as client:
                try:
                    response = await client.get(url)
                    response.raise_for_status()
                    return response
                except httpx.HTTPError as error:
                    error_message = f"Could not make call with method: {method}, url: {url}. Error: {error}"
                    self.logger.error(error_message)
                    if raise_error:
                        self.raise_error(error_message)

        elif method == "post":
            async with httpx.AsyncClient() as client:
                try:
                    response = await client.post(url, json=body)
                    response.raise_for_status()
                    return response
                except httpx.HTTPError as error:
                    error_message = f"Could not make call with method: {method}, url: {url}, body: {body}. Error: {error}"
                    self.logger.error(error_message)
                    if raise_error:
                        self.raise_error(error_message)

        elif method == "put":
            async with httpx.AsyncClient() as client:
                try:
                    response = await client.put(url, json=body)
                    response.raise_for_status()
                    return response
                except httpx.HTTPError as error:
                    error_message = f"Could not make call with method: {method}, url: {url}. Error: {error}"
                    self.logger.error(error_message)
                    if raise_error:
                        self.raise_error(error_message)
        else:
            self.logger.error(
                detail=f"Httpx wrapper not found method: {method}",
            )
