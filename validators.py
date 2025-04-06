from pydantic import BaseModel, validator

class TaskSchema(BaseModel):
    name: str

    @validator('name')
    def not_empty(cls, v):
        if not v: raise ValueError('Name required')
        return v