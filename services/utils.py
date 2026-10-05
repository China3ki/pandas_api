from pathlib import Path

import pandas as pd


def convert_to_dataframe(filename : str):
    file_path = Path(__file__).resolve().parent.parent / "files" / filename
    file_extension = filename.split(".")[-1].lower()
    try:
        if file_extension == "json":
            return pd.read_json(file_path)
        elif file_extension == "csv":
            return pd.read_csv(file_path)
        elif file_extension == "xlsx":
            return pd.read_excel(file_path)
    except FileNotFoundError:
        return None





