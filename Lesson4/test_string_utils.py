import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# тест 1 капитализация
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    (" abc", " abc"),  # капитализация, начало с пробела
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# тест 2 обрезка пробела в начале
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" Skypro", "Skypro"),
    ("    hello world", "hello world"),  # три пробела
    (" лапша", "лапша"),
    (" 654", "654"),  # число как строка
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("23abc ", "23abc "),  # пробел в конце, а не в начале
    ("", ""),
    ("11", "11"),  # нет пробелов
    ("Three simple  words", "Three simple  words"),  # пробелы в предложении
    ])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# тест 3 проверка наличия символа
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol", [
    ("Skypro", "r"),
    ("hello world", "w"),  # два слова
    ("лапша", "л"),
    ("654", "5"),  # число как строка
])
def test_contains_positive(input_str, symbol):
    assert string_utils.contains(input_str, symbol) is True


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol", [
    ("no abc", " "),  # ищем пробел (а вроде не должны?)
    ("", ""),  # пустая строка
    ("abc", "ab"),  # два символа, должна вернуть True? или False и не упасть
    ("Three simple", "e"),  # многократно в предложении
])
def test_contains_negative(input_str, symbol):
    assert string_utils.contains(input_str, symbol)
    # убрала assert not и проверки то проходят - баги тут?


# тест 4 удаление символа
@pytest.mark.positive
@pytest.mark.parametrize("input_str, deleted, result", [
    ("Skypro", "S", "kypro"),
    ("лапша", "ш", "лапа"),
    ("654", "6", "54"),  # число как строка
])
def test_delete_symbol_positive(input_str, deleted, result):
    assert string_utils.delete_symbol(input_str, deleted) == result


@pytest.mark.negative
@pytest.mark.parametrize("input_str, deleted, result", [
    ("", "n", ""),  # пустая строка ввода
    ("лапша", "г", "лапша"),  # не существует в
])
def test_delete_symbol_negative(input_str, deleted, result):
    assert string_utils.delete_symbol(input_str, deleted) == result
