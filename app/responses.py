from pydantic import BaseModel


class ErrorResponse(BaseModel):
    error: str


error_response_422 = {422: {"model": ErrorResponse, "description": "Validation error"}}
error_response_404 = {404: {"model": ErrorResponse, "description": "Object not found"}}
