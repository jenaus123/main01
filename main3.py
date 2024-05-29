user_input = input("enter a number")
user_number = int(user_input)

digit1 = user_number % 10
value = user_number // 10
digit1 = digit1 * 10000
digit2 = value % 10
value = value // 10
digit2 = digit2 * 1000
digit3 = value % 10
value = value // 10
digit3 = digit3 * 100
digit4 = value % 10
value = value // 10
digit4 = digit4 * 10
digit5 = value
result = digit1 + digit2 + digit3 + digit4 + digit5

print(result)