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

    for s0 in input_string.split("("):
        for s1 in s0.split(")"):
            if s1.count("[") != s1.count("]"):
                return False
            elif s1.count("{") != s1.count("}"):
                return False
    for s0 in input_string.split("["):
        for s1 in s0.split("]"):
            if s1.count("(") != s1.count(")"):
                return False
            elif s1.count("{") != s1.count("}"):
                return False

    for s0 in input_string.split("{"):
        for s1 in s0.split("}"):
            if s1.count("[") != s1.count("]"):
                return False
            elif s1.count("(") != s1.count(")"):
                return False
    return True
