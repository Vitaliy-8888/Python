import pytest
from number_list_comparator import NumberListComparator

def test_compare_lists_reverse():
    list1 = [10, 9, 8, 7, 6]
    list2 = [5, 4, 3, 2, 1]
    comparator = NumberListComparator(list1, list2)
    assert comparator.compare_lists() == "Первый список имеет большее среднее значение"

def test_compare_lists_different_lengths():
    list1 = [1, 2, 3, 4]
    list2 = [5, 6, 7, 8, 9, 10]
    comparator = NumberListComparator(list1, list2)
    assert comparator.compare_lists() == "Второй список имеет большее среднее значение"

def test_compare_lists_all_zeroes():
    list1 = [0, 0, 0, 0]
    list2 = [0, 0, 0, 0]
    comparator = NumberListComparator(list1, list2)
    assert comparator.compare_lists() == "Средние значения равны"

def test_compare_lists_single_element():
    list1 = [100]
    list2 = [200]
    comparator = NumberListComparator(list1, list2)
    assert comparator.compare_lists() == "Второй список имеет большее среднее значение"
    