def fun_divide(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print('Ты не можешь делить на 0!')

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

result_divide = fun_divide(num1, num2)
print(result_divide)

