from fastapi import APIRouter

from dto.add_column_dto import AddColumn

data_router = APIRouter(
    prefix="/data"
)
@data_router.post("/addcolumn")
def add_column(filename: str, new_column: AddColumn):
        pass
