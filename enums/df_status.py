from enum import Enum


class DataStatus(Enum):
    OK = "ok"
    DF_DOES_NOT_EXIST = "File does not exist"
    INCORRECT_VALUE = "Incorrect value"
    NOT_VALID_TOKENS = "Not valid tokens"
    COLUMN_DOES_NOT_EXIST = "Column does not exist"
    CANNOT_DEVICE_BY_0 = "Cannot divide by 0"
    WRONG_OPERATION = "Wrong math operation"
    COLUMN_EXIST = "Column already exist!"
    EMPTY_COLUMN = "Column cannot be empty!"
    EXTENSION_NOT_SUPPORTED = "Extension is not supported!"
    COLUMNS_NOT_UNIQUE = "Cannot have two same columns names"
    INDEX_NOT_MATCH = "Index does not match"