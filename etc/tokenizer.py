import pandas as pd


def convert_to_tokens(user_value: str, df: pd.DataFrame) -> list[str]:
    user_value = user_value.replace(" ", "")
    tokens = []
    bufor = ""
    operators = ["+", "-", "*", "/"]
    for i, token in enumerate(user_value):
        if token in operators:
            tokens.append(bufor)
            tokens.append(token)
            bufor = ""
            continue
        bufor += token
        if i == len(user_value) - 1:
            tokens.append(bufor)

    tokens = convert_to_series(df, tokens)
    return tokens

def calculate_loop(tokens: list[str]):
    operators_priority = {"+": 1, "-": 1, "*": 2, "/": 2}
    while len(tokens) > 1:
        index = -1
        priority = -1
        for i, token in enumerate(tokens):
            if not isinstance(token, pd.Series) and priority < operators_priority.get(token, -1):
                priority = operators_priority[token]
                index = i
        tokens = calculate(tokens, index)
    return tokens[0]


def calculate(tokens: list[str], index):
    left_number, right_number = convert_numbers(tokens[index - 1], tokens[index + 1])
    operator = tokens[index]
    result = ""
    match operator:
        case "+":
            result = left_number + right_number
        case "-":
            result = left_number - right_number
        case "*":
            result = left_number * right_number
        case "/":
            result = left_number / right_number

    tokens[index - 1] = result
    del tokens[index + 1]
    del tokens[index]
    return tokens


def convert_to_series(df, tokens):
    operators = ["+", "-", "*", "/"]
    for i, token in enumerate(tokens):
        if token not in operators and not check_is_float(token):
            tokens[i] = df[token]
    return tokens

def convert_numbers(left_number : str | pd.Series, right_number : str | pd.Series):
    if not isinstance(left_number, pd.Series):
        left_number = float(left_number)
    if not isinstance(right_number, pd.Series):
        right_number = float(right_number)

    return left_number, right_number

def check_is_float(number: str):
    try:
        number = float(number)
        return True
    except ValueError:
        return False