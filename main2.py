
user_input = input("enter a number: ")
user_number = int(user_input)
digit1, value = divmod(user_number, 1000)
digit2, value = divmod(value, 100)
digit3, value = divmod(value, 10)
print(digit1)
print(digit2)
print(digit3)
print(value)

