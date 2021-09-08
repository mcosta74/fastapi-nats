from pydantic import BaseModel


class UppercaseRequest(BaseModel):
    message: str


class UppercaseResponse(BaseModel):
    results: str
