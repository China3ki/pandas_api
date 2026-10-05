from pydantic import (
    BaseModel, Field
)


class AddColumn(BaseModel):
    column_name: str = Field(min_length=1)
    value: str | None = None