from pathlib import Path

import pandas as pd


def convert_to_dataframe(filename : str) -> tuple[bool, pd.DataFrame | None]:
    """ Konwertuje plik na dataframe """
    file_path = Path(__file__).resolve().parent.parent / "files" / filename
    file_extension = filename.split(".")[-1].lower()
    try:
        if file_extension == "json":
            return True, pd.read_json(file_path)
        elif file_extension == "csv":
            return True, pd.read_csv(file_path)
        elif file_extension == "xlsx":
            return True, pd.read_excel(file_path)
    except FileNotFoundError:
        return False, None



def convert_to_series(series_str: str, df: pd.DataFrame):
    converted_string = series_str[2: -1]
    try:
        series = df[converted_string]
        return True, series
    except KeyError:
        return False, f"Column '{converted_string}' does not exist!"


