from dto.add_column_dto import AddColumn
from etc.tokenizer import tokenizer, validate_tokens
from services.file_service import save_existed_files
from services.utils import convert_to_dataframe, convert_to_series
import pandas as pd

def add_column_service(filename: str, new_column: AddColumn):
    df_is_valid, df, file_error_message = convert_to_dataframe(filename)
    if not df_is_valid:
        return False, file_error_message

    if new_column.value is None or new_column.value.lower() == "null":
        df[new_column.column_name] = new_column.value
        save_existed_files(df, filename)
        return True, f"Column {new_column.column_name} has been added"

    if not new_column.value.startswith("="):
        df[new_column.column_name] = new_column.value
        save_existed_files(df, filename)
        return True, f"Column {new_column.column_name} has been added"

    tokens = tokenizer(new_column.value)
    is_valid, error_message = validate_tokens(tokens)
    if not is_valid:
        return error_message


    if len(tokens) == 1: # Sprawdza, czy istnieje tylko jeden token. Jeśli tak konwertuję na właściwy typ danych
        is_valid, value = convert_to_number(tokens[0], df)
        if not is_valid:
            return value
        df[new_column.column_name] = value
        save_existed_files(df, filename)
        return True, f"Column '{new_column.column_name}' has been added"


    value_is_valid, value = calculate_loop(tokens, df)


    if value_is_valid:
        df[new_column.column_name] = value
    else:
        return False, "Column does not exist!"
    save_existed_files(df, filename)
    return True, f"Column '{new_column.column_name}' has been added"



def calculate_loop(tokens: list[str], df: pd.DataFrame):
    operators = { "+": 1, "-": 1, "*": 2, "/":2 }

    while len(tokens) > 1:
        index = -1
        priority = -1
        for i, token in enumerate(tokens):
            if not isinstance(token, pd.Series) and token in operators:
                if operators.get(token, -1) > priority:
                    priority = operators.get(token, -1)
                    index = i

        correct_value = calculate(tokens, index, df)
        if correct_value is False:
            return False, -1
    return True, tokens[0]


def calculate(tokens: list[str], operator_index: int, df: pd.DataFrame):
    left_is_valid, left_number = convert_to_number(tokens[operator_index - 1], df)
    right_is_valid, right_number = convert_to_number(tokens[operator_index + 1], df)
    if left_is_valid is False or right_is_valid is False:
        return False
    operator = tokens[operator_index]
    result = 0
    match operator:
        case "+":
            result = left_number + right_number
        case "-":
            result = left_number - right_number
        case "*":
            result = left_number * right_number
        case "/":
            result = left_number / right_number

    tokens[operator_index - 1] = result
    del tokens[operator_index]
    del tokens[operator_index]

    return True




def convert_to_number(token: str, df: pd.DataFrame):
    if not isinstance(token,float) and not isinstance(token, pd.Series) and token.startswith("c["):
        series_is_valid, series = convert_to_series(token, df)
        return series_is_valid, series
    elif not isinstance(token, pd.Series):
        return True,float(token)

    return True, token










