from fastapi import APIRouter, UploadFile, HTTPException

from dto.new_file_dto import NewFileDto
from enums.df_status import DataStatus
from services.file_service import verify_file, upload_file, delete_file, create_new_file

file_router = APIRouter(
    prefix="/file"
)


@file_router.post("/upload")
async def upload(file: UploadFile):
    if not verify_file(file):
        raise HTTPException(status_code=404, detail="File not supported")
    file_name = await upload_file(file)
    return { "Saved": "Ok", "Filename": file_name }

@file_router.post("/create")
def create(new_file_dto: NewFileDto):
    status, filename = create_new_file(new_file_dto)
    if status != DataStatus.OK:
        raise HTTPException(status_code=400, detail=status.value)
    return {"Saved": "Ok", "Filename": filename}



@file_router.delete("/{filename}")
def delete(filename: str):
    delete_file_api = delete_file(filename)
    if not delete_file_api:
        raise HTTPException(status_code=404, detail="File not found")
    return { "Status": f"{filename} has been removed."}

