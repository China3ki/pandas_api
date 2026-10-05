from fastapi import APIRouter, UploadFile, HTTPException

from services.file_service import verify_file, upload_file, delete_file

file_router = APIRouter(
    prefix="/file"
)


@file_router.post("/")
async def upload(file: UploadFile):
    if not verify_file(file):
        raise HTTPException(status_code=404, detail="File not supported")
    return await upload_file(file)


@file_router.delete("/{filename}")
async def delete(filename: str):
    delete_file_api = delete_file(filename)
    if delete_file_api is None:
        raise HTTPException(status_code=404, detail="File not found")
    return delete_file(filename)
