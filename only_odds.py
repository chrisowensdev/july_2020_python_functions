list1 = [11, 20, 42, 97, 23, 10]


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def is_odd(num):
    if is_even(num) == True:
        return False
    else:
        return True


def only_odds(lst):
    odds_list = []
    for num in lst:
        if is_odd(num):
            odds_list.append(num)
    return odds_list


print(only_odds(list1))
