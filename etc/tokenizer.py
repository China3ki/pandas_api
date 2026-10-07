def tokenizer(user_input: str):
    operators = ["+", "-", "*", "/"]
    bufor = ""
    tokens = []
    user_input = user_input.strip()
    for i, token in enumerate(user_input):
        if not bufor.startswith("c["):
            bufor = bufor.strip()
        if token in operators:
            if bufor.startswith("c["):
                bufor += token
                continue
            if token == "-" and bufor.strip() == "" and (i == 0 or tokens[-1] in operators): # Sprawdza, czy obecny token jest "-" i czy ostatni dodany token jest w operatorach lub i wynosi 0.
                bufor += "-"
                continue

            if bufor.strip() != "": ## Przycina spacje buforu, aby nie dodawał się do listy tokenów pusty token.
                tokens.append(bufor)
            tokens.append(token)
            bufor = ""
            continue
        bufor += token
        if bufor.endswith("]"):
            tokens.append(bufor)
            bufor = ""
            continue
        if i == len(user_input) -1:
            tokens.append(bufor)
    print(tokens)
    cleared_tokens = clear_tokens(tokens)
    return cleared_tokens

def clear_tokens(tokens : list[str]):
    cleared_tokens = []
    for token in tokens:
        token = token.strip()
        if token.startswith("c[") and token.endswith("]"):
            cleared_tokens.append(token)
            continue
        cleared_token = token.replace(" ", "")
        cleared_tokens.append(cleared_token)

    return cleared_tokens

def validate_tokens(tokens: list[str]):
    """ Weryfikuję czy tokeny są w poprawnej kolejności"""
    operators = ["+", "-", "*", "/"]

    if len(tokens) == 0:
        return False, f"Empty operation"


    for i, token in enumerate(tokens):
        if i % 2 == 0:
            if not check_is_float(token) and (not token.startswith("c[") or not token.endswith("]")):
                return False, f"Wrong operation in {tokens} - token index = {i}"
        if i % 2 == 1:
            if not token in operators:
                return False, f"Wrong operation in {tokens} - token index = {i}"
            if token == tokens[-1]:
                return False, f"Wrong operation in {tokens} - token index = {i}"
            if token == "/" and tokens[i + 1] == "0":
                return False, f"Cannot divide by 0 in {tokens} token index = {i}"
    return True

def check_is_float(token: str):
    try:
        float(token)
        return True
    except ValueError:
        return False

tokens1 = tokenizer("2 + c[cena-netto]")

print(tokens1)
print(validate_tokens(tokens1))