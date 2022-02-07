my_list = []


while True:
    user_elem = input('Write information: ')
    if user_elem == ' ':
        print(my_list)
        exit()
    else:
        my_list.append(user_elem + '\n')


    with open('task_51.txt', 'w') as file_obj:
        file_obj.writelines(my_list)
