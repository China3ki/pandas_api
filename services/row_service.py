from enums.df_status import DataStatus
from services.file_service import save_existed_files
from services.utils import convert_to_dataframe
import pandas as pd

def add_row(filename: str, rows: list[dict]):
    """ Dodaje nowy wiersz do dataframe"""
    is_valid, df = convert_to_dataframe(filename)
    if not is_valid or df is None:
        return DataStatus.DF_DOES_NOT_EXIST
    df_columns = df.columns.to_list()

    for row in rows:
        for key, value in row.items():
            if key not in df_columns:
                return DataStatus.COLUMN_DOES_NOT_EXIST
        df.loc[len(df)] = row

    save_existed_files(df, filename)
    return DataStatus.OK
def remove_row(filename: str, row_index: int):
    is_valid, df = convert_to_dataframe(filename)
    if not is_valid or df is None:
        return DataStatus.DF_DOES_NOT_EXIST

    if 0 > row_index and row_index > len(df) - 1:
        return DataStatus.INDEX_NOT_MATCH
    df = df.drop(row_index)
    df = df.reset_index(drop=True)
    save_existed_files(df, filename)
    return DataStatus.OK
