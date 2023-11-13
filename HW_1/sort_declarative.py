# Дан список целых чисел numbers. Необходимо написать в декларативном стиле процедуру для
# сортировки числа в списке в порядке убывания.
def sort_list_declarative(numbers):
    numbers.sort(reverse=True)
    return numbers


if __name__ == '__main__':
    numbers = [53, 18, -9, 7, 0, 13]
    print(sort_list_declarative(numbers))
