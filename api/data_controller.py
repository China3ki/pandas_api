from fastapi import APIRouter, HTTPException

from dto.add_column_dto import AddColumn
from services.data_service import add_column_service

data_router = APIRouter(
    prefix="/data"
)


@data_router.post("/addcolumn")
def add_column(filename: str, new_column: AddColumn):
    is_valid, message = add_column_service(filename, new_column)
    if not is_valid:
        raise HTTPException(status_code=404, detail=message)

    return message
