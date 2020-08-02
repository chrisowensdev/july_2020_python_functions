list1 = [11, 20, 42, 97, 23, 10]


def only_evens(lst):
    even_list = []
    for num in lst:
        if num % 2 == 0:
            even_list.append(num)
    return even_list


print(only_evens(list1))
