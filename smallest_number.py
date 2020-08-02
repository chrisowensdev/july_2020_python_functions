list1 = [34, 56, 2, 67, 45, 100]


def smallest_number(lst):
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest


print(smallest_number(list1))
