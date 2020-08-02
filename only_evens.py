list1 = [11, 20, 42, 97, 23, 10]


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def only_evens(lst):
    even_list = []
    for num in lst:
        if is_even(num):
            even_list.append(num)
    return even_list


print(only_evens(list1))
