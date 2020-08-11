list1 = ["on", "two", "three"]


def longest_string(lst):
    long_string = lst[0]
    for string in lst:
        if len(string) > len(long_string):
            long_string = string
    return long_string


print(longest_string(list1))
