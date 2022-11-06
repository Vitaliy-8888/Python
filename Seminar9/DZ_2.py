import pytest
from nok_def import nok
from nod_def import nod


list_example = [(1, 5, 1), (5, 47, 1)]
list_example2 = [(1, 5, 5), (5, 47, 235)]


@pytest.mark.parametrize('a, b, result', list_example2)
def test_num_nok_good(a, b, result):
    assert nok(a, b) == result

@pytest.mark.parametrize('a, b, result', list_example)
def test_num_nod_good(a, b, result):
    assert nod(a, b) == result
    