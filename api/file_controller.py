from fastapi import APIRouter, UploadFile

from services.file_service import verify_file, upload_file, delete_file

file_router = APIRouter(
    prefix="/file"
)

@file_router.post("/")
async def upload(file : UploadFile):
        if not verify_file(file):
            return "File not supported"
        return await upload_file(file)

@file_router.delete("/")
async def delete(filename: str):
    return delete_file(filename)
