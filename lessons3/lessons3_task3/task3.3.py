def my_func(num1, num2, num3):
    my_list = [num1, num2, num3]
    result_list = []
    min_1 = min(my_list)
    result_list.append(min_1)
    my_list.remove(min_1)
    return sum(my_list)

result = my_func(2, 10, 13)

print(result)