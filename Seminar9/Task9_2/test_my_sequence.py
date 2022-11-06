# Задача ДЗ 9_2. Написать тесты к функциям из ранее выполненных заданий.

import pytest
from my_sequence import num_sequence

# мы передаем элементы в последовательность (1 + 1/n)^n  
# ожидавемый результат = 11.55 (или 14.07)
list_example = [(5, 11.55), (6, 14.07)]    

@pytest.mark.parametrize('a, expected_result', list_example)   # в list_example передаются занчения из списка
def test_num_sequence_good(a, expected_result):  
    assert num_sequence(a) == expected_result    

# expected result - ожидаемый результат
# если передадим переменной х значение = '2' (строка, а не число), то будет ошибка типа данных (TypeError)
@pytest.mark.parametrize('expected_exception, x', [(TypeError, '2')])   
def test_num_sequence_with_error(expected_exception, x):  
    with pytest.raises(expected_exception):     # expected_exception - ожидаемое исключение
        num_sequence(x)  
