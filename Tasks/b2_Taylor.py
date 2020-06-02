"""
Taylor series
"""
from typing import Union
from itertools import count
from math import factorial

DELTA = 0.0001


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    total = 0
    for n in count():
        f = (x ** n) / factorial(n)
        total += f
        if f <= DELTA:
            break

    return total


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    total = x
    n = 3
    cnt = 1
    while True:
        f = (x ** n) / factorial(n)
        n += 2
        if cnt % 2:
            total -= f
        else:
            total += f
        cnt += 1
        if f <= DELTA:
            break

    return total
