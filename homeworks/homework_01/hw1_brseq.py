#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
    '''
    сделан на основе кода со stackoverflow, можно не засчитывать баллы
    '''
    opening = "([{"
    closing = ")]}"
    stack = []  # стек для скобок

    for character in input_string:
        if character in opening:  # открывающая скобка
            stack.append(opening.index(character))  # индекс скобки в opening
        elif character in closing:  # закрывающая скобка
            if stack and stack[-1] == closing.index(character):  # тот же тип скобок
                stack.pop()  # удаляем
            else:
                return False  # не тот тип

    return not stack  # not на случай если только открывающиеся
