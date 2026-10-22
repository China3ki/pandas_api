from services.utils import convert_to_dataframe


def file_info(filename : str):
    is_valid, df = convert_to_dataframe(filename)
    if not is_valid:
        return None
    headers = list(df.columns)
    rows = len(df.index)
    return {"Headers": headers, "Columns": len(headers), "Rows": rows, "Filename": filename}