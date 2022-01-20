user_numbers = int(input('Введите целое положительное число: '))

numb = 0

while user_numbers > 0:
    number = user_numbers % 10
    if number > numb:
        numb = number
    user_numbers = user_numbers // 10

print(numb)


