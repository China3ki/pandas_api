from dto.add_column_dto import AddColumn
from services.utils import convert_to_dataframe


def add_column(filename: str, new_column: AddColumn):
    df = convert_to_dataframe(filename)
    if new_column.value is None or new_column.value.lower() == "null":
        pass

    if not new_column.value.startswith("="):
        pass
        return

new = AddColumn(column_name="fajna kolumna", value=None)
add_column("66e5f6d4d22e43c3bcd81e08c7467209.csv", new)










