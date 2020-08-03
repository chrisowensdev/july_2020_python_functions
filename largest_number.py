list1 = [34, 56, 2, 67, 45, 100]


def largest_number(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest


print(largest_number(list1))
