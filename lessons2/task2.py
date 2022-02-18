user_count = int(input('Введите количество элементов: '))

user_list = []

while user_count > 0:
    user_elem = input('Введите значение: ')
    user_list.append(user_elem)
    user_count -= 1

for i in range(0, len(user_list) - 1, 2):
    user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]

print(user_list)




