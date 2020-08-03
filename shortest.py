list1 = ["on", "two", "three"]


def shortest_string(lst):
    short_string = lst[0]
    for string in lst:
        if len(string) < len(short_string):
            short_string = string
    return short_string


print(shortest_string(list1))
