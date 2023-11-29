"""
Парадигмы: процедурная - для удобства использования и переиспользования, структурная - для лучшего контроля и "отлова"
ошибок))
"""


def binary_search(lst: list, num: int) -> int:
    start = 0
    end = len(lst) - 1
    while start <= end:
        middle = (start + end) // 2
        if lst[middle] == num:
            return middle
        elif lst[middle] < num:
            start = middle + 1
        else:
            end = middle - 1
    return -1


if __name__ == '__main__':
    lst = [-4, 5, 17, 48, 103, 620]
    num = 17
    # num = 55
    print(binary_search(lst, num))

