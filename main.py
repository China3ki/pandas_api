from fastapi import  FastAPI
from api.file_controller import file_router
from api.info_controller import info_router

app = FastAPI()
app.include_router(file_router)
app.include_router(info_router)