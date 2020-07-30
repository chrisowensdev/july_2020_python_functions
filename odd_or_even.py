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


user_input = int(input("Is the number even: "))
even = is_even(user_input)

print(even)
