from main import division
import pytest


@pytest.mark.parametrize('a, b, expected_result', [(6, 3, 2),
                                                   (10, 2, 5),
                                                   [30, -3, -10]])
# Декоратор используются при неоднакратном использовании атомарного теста
# Позитивный тест
def test_divisiov_good(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize('a, b, expected_exception', [(6, 0, ZeroDivisionError),
                                                    (10, '2', TypeError)])
# Негативный тест на ожидание ошибки
def test_divisiov_error(a, b, expected_exception):
    with pytest.raises(expected_exception): # контексный менеджер, который ожидает исключения
        division(a, b)

# --collect-only - вывод списка найденных




