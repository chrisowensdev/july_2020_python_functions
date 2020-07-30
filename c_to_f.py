def celsius_to_fahrenheit(temp):
    fahrenheit = (temp * 9/5) + 32
    return fahrenheit


user_input = float(input("Temp to Fahrenheit? "))
temp_conversion = celsius_to_fahrenheit(user_input)

print(temp_conversion)
