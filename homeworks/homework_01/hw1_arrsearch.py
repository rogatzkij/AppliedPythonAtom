#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    '''
    Метод возвращает индексы двух различных
    элементов listа, таких, что сумма этих элементов равна
    n. В случае, если таких элементов в массиве нет,
    то возвращается None
    Ограничение по времени O(n)
    :param input_list: список произвольной длины целых чисел
    :param n: целевая сумма
    :return: tuple из двух индексов или None
    '''
    first = 0
    last = len(input_list) - 1

    input_list.sort()

    for i in range(len(input_list)):
        val = input_list[first] + input_list[last]
        if first < 0 or last >= len(input_list):
            break
        elif val == n:
            answer = (first, last)
            return answer
        elif val > n:
            last -= 1
        elif val < n:
            first += 1
    return None
