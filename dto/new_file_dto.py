from pydantic import (
    BaseModel, Field
)


class NewFileDto(BaseModel):
    columns: list[str] = Field(min_length=1)
    extension: str