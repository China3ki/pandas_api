from services.utils import convert_to_dataframe


def file_info(filename : str):
    df = convert_to_dataframe(filename)
    if df is None:
        return None
    headers = list(df.columns)
    rows = len(df.index)
    return {"Headers": headers, "Columns": len(headers), "Rows": rows, "Filename": filename}