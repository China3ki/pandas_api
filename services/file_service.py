import os
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile


def verify_file(file: UploadFile) -> bool:
    """ Weryfikuje pliki. Jeśli plik ma rozszerzenie json, csv lub xlsx, zwraca True w innym przypadku False."""
    file_extension = get_file_extension(file)
    if file_extension == "json" or file_extension == "csv" or file_extension == "xlsx":
        return True
    else:
        return False

async def upload_file(file : UploadFile) -> dict:
    save_path = Path(__file__).resolve().parent.parent / "files"
    if not save_path.exists():
        os.mkdir(save_path)
    content = await file.read()
    file_name = f"{uuid4().hex}.{get_file_extension(file)}"
    save_path = save_path / file_name
    save_path.write_bytes(content)
    return { "Saved": "Ok", "Filename": file_name }



def delete_file(filename: str) :
    """ Usuwa plik podany przez użytkownika """
    file_path = Path(__file__).resolve().parent.parent / "files" / filename
    try:
        os.remove(file_path)
        return { "Status": f"{filename} has been removed."}
    except FileNotFoundError:
        return None


def get_file_extension(file: UploadFile):
    """ Zwraca rozszerzenie pliku przesłanego przez użytkownika."""
    return file.filename.split(".")[-1].lower()
