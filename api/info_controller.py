from fastapi import APIRouter, HTTPException

from services.file_info_service import file_info

info_router = APIRouter(
    prefix="/info"
)

@info_router.get("/{filename}")
async def get_file_info(filename: str):
    info = file_info(filename)
    if info is None:
        raise HTTPException(status_code=404, detail="File not found or file data is not supported")
    return file_info(filename)
