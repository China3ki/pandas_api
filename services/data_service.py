from dto.add_column_dto import AddColumn
from etc.tokenizer import convert_to_tokens, calculate_loop, convert_to_series
from services.utils import convert_to_dataframe


def add_column(filename: str, new_column: AddColumn):
    df = convert_to_dataframe(filename)
    tokens = []
    if new_column.value is not None:
        tokens = convert_to_tokens(new_column.value, df)
    calculation = calculate_loop(tokens)
    df[new_column.column_name] = calculation

    print(df)




new = AddColumn(column_name="fajna kolumna", value="15 + 1 * rating")

add_column("66e5f6d4d22e43c3bcd81e08c7467209.csv", new)


