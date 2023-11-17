import pytest
from translator import Translator

translate_testdata = [
    ("Не ищи счастье – оно всегда у тебя внутри", "Яна заўсёды ў цябе ўнутры"),
    ("Отличная сегодня погода!", "Выдатная сёння надвор'е!"),
]


@pytest.mark.parametrize("input,expected_output", translate_testdata)
def test_translate(input, expected_output):
    t = Translator()

    output = t.translate(input)

    assert output == expected_output
