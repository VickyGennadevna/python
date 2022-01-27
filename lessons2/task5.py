my_lists = [7, 5, 3, 3, 2]

user_elem = int(input('Введите натуральное число: '))

for i in range(len(my_lists)):
    if user_elem == my_lists[i]:
        my_lists.insert(i + 1, user_elem)
        break
    elif user_elem > my_lists[0]:
        my_lists.insert(0, user_elem)
    elif user_elem < my_lists[-1]:
        my_lists.append(user_elem)
    elif user_elem < my_lists[i] and user_elem > my_lists[i + 1]:
        my_lists.insert(i + 1, user_elem)
        break

print(my_lists)


