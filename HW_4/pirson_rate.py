from functools import reduce
from math import sqrt
from typing import List
import numpy as np


def difference(arr: List):
    aver = sum(arr) / len(arr)
    new_arr = [elem - aver for elem in arr]
    return new_arr


def square_diff(arr: List):
    sq_dif = list(map(lambda x: x ** 2, arr))
    return sq_dif


def numerator(arr_x: List, arr_y: List):
    dif_x = difference(arr_x)
    dif_y = difference(arr_y)
    result = list(map(lambda x, y: x * y, dif_x, dif_y))
    result_numerator = reduce(lambda x, y: x + y, result)
    return result_numerator


def denominator(arr_x: List, arr_y: List):
    dif_x = difference(arr_x)
    dif_y = difference(arr_y)
    sq_dif_x = square_diff(dif_x)
    sq_dif_y = square_diff(dif_y)
    sum_x = reduce(lambda x, y: x + y, sq_dif_x)
    sum_y = reduce(lambda x, y: x + y, sq_dif_y)
    result = sqrt(sum_x * sum_y)
    return result


def pirson_rate(numer, denomin):
    result = numer / denomin
    return result


if __name__ == '__main__':
    arr_1 = [3, 5, 2]
    arr_2 = [2, 0, 7]
    numer = numerator(arr_1, arr_2)
    denomin = denominator(arr_1, arr_2)
    print(pirson_rate(numer, denomin))
    #print(np.corrcoef(arr_1, arr_2)[0,1])
