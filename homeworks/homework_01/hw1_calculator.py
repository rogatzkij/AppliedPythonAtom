#!/usr/bin/env python
# coding: utf-8
import numbers


def calculator(x, y, operator):
    '''
    Простенький калькулятор в прямом смысле. Работает c числами
    :param x: первый агрумент
    :param y: второй аргумент
    :param operator: 4 оператора: plus, minus, mult, divide
    :return: результат операции или None, если операция не выполнима
    '''
    if isinstance(x, numbers.Number) == False:
        return None
    if isinstance(y, numbers.Number) == False:
        return None

    if operator == "plus":
        return x + y
    if operator == "minus":
        return x - y
    if operator == "mult":
        return x * y
    if operator == "divide":
        if y == 0:
            return None
        return x / y
    return None
