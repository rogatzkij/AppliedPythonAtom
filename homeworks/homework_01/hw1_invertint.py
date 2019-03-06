#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    isNegative = number<0

    if isNegative:
        number = -number

    result = 0
    while number != 0:
        result = result*10 + number%10
        number = number // 10

    if isNegative:
        return -result
    return result
