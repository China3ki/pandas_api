import os
from pathlib import Path
from uuid import uuid4

import pandas as pd
from fastapi import UploadFile

from dto.new_file_dto import NewFileDto
from enums.df_status import DataStatus


def verify_file(file: UploadFile) -> bool:
    """ Weryfikuje pliki. Jeśli plik ma rozszerzenie json, csv lub xlsx, zwraca True w innym przypadku False."""
    file_extension = get_file_extension(file)
    if file_extension == "json" or file_extension == "csv" or file_extension == "xlsx":
        return True
    else:
        return False

def create_folder():
    save_path = Path(__file__).resolve().parent.parent / "files"
    if not save_path.exists():
        os.mkdir(save_path)

async def upload_file(file : UploadFile) -> str:
    """ Uploaduje plik wysłany przez api do folderu files."""
    save_path = Path(__file__).resolve().parent.parent / "files"
    create_folder()
    content = await file.read()
    file_name = f"{uuid4().hex}.{get_file_extension(file)}"
    save_path = save_path / file_name
    save_path.write_bytes(content)
    return file_name


def save_existed_files(df: pd.DataFrame, filename : str):
    """ Nadpisuję istniejący już plik """
    save_path = Path(__file__).resolve().parent.parent / "files" / filename
    file_extension = filename.split(".")[1]
    create_folder()
    match file_extension:
        case "csv":
            pd.DataFrame.to_csv(df, path_or_buf=save_path, index=False)
        case "json":
            pd.DataFrame.to_json(df, path_or_buf=save_path, index=False)
        case "xlsx":
            pd.DataFrame.to_excel(df, save_path, index= False)


def create_new_file(new_file_dto: NewFileDto):
    extensions = ["csv", "json", "xlsx"]
    if new_file_dto.extension not in extensions:
        return DataStatus.EXTENSION_NOT_SUPPORTED, ""
    cleared_list = [value.strip() for value in new_file_dto.columns]
    if "" in cleared_list:
        return DataStatus.EMPTY_COLUMN, ""
    unique_columns = set(cleared_list)
    if len(unique_columns) != len(cleared_list):
        return DataStatus.COLUMNS_NOT_UNIQUE, ""

    df = pd.DataFrame(columns=cleared_list)
    filename = f"{uuid4().hex}.{new_file_dto.extension}"
    save_existed_files(df, filename)
    return DataStatus.OK, filename


def delete_file(filename: str) :
    """ Usuwa plik podany przez użytkownika """
    file_path = Path(__file__).resolve().parent.parent / "files" / filename
    try:
        os.remove(file_path)
        return True
    except FileNotFoundError:
        return False


def get_file_extension(file: UploadFile):
    """ Zwraca rozszerzenie pliku przesłanego przez użytkownika."""
    return file.filename.split(".")[-1].lower()

