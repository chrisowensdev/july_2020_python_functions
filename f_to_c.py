def fahrenheit_to_celsius(temp):
    celsius = (temp - 32) * 5/9
    return celsius


user_input = float(input("Temp to Celcius? "))
temp_conversion = fahrenheit_to_celsius(user_input)
print(int(temp_conversion))
