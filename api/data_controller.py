from fastapi import APIRouter, HTTPException

from dto.column_dto import ColumnDto
from enums.df_status import DataStatus
from services.data_service import data_service, delete_column_service
from services.row_service import add_row, remove_row

data_router = APIRouter(
    prefix="/data"
)


@data_router.post("/addcolumn")
def add_column(filename: str, new_column: ColumnDto):
    status = data_service(filename, new_column, False)
    if status is not DataStatus.OK:
        raise HTTPException(status_code=404, detail=status.value)
    return { "Status": f"Column '{new_column.column_name}' has been added" }
@data_router.put("/editcolumn")
def edit_column(filename: str, column: ColumnDto):
    status = data_service(filename, column, True)
    if status is not DataStatus.OK:
        raise HTTPException(status_code=404, detail=status.value)
    return { "Status": f"Column '{column.column_name}' has been edited" }

@data_router.delete("/deletecolumn")
def delete_column(filename:str, column_name: str):
    status = delete_column_service(filename, column_name)
    if status is not DataStatus.OK:
        raise HTTPException(status_code=404, detail=status.value)
    return { "Status:" f"Column '{column_name}' has been deleted" }

@data_router.post("/addrow")
def add_data_api(filename: str, rows: list[dict]):
    status = add_row(filename, rows)
    if status is not DataStatus.OK:
        raise HTTPException(status_code=404, detail=status.value)
    return {"Status:" f"Column has been added!"}

@data_router.delete("/removerow")
def delete_row_api(filename: str, row_index: int):
    status = remove_row(filename, row_index)
    if status is not DataStatus.OK:
        raise HTTPException(status_code=404, detail=status.value)
    return {"Status:" f"Column {row_index} been deleted!"}



