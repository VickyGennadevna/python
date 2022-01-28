def my_sum(user_number):
    result_sum = 0
    user_exit = False
    while user_exit == False:
        number_zero = 0
        numbers = input('Введите строку чисел через пробел или нажмите R: ').split()
        for i in range(len(numbers)):
            if numbers[i] == 'R':
                user_exit = True
                break
            else:
                number_zero = number_zero + int(numbers[i])
        result_sum = result_sum + number_zero
        print(f'Ваша сумма на данный момент: {result_sum}')

    return result_sum

result = my_sum()
print(f'Ваша сумма чисел {result}')