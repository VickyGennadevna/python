my_list = ['Vika\n', 'Kate\n', 'Dima\n']

with open('task2_2', 'w+') as file_obj:
    file_obj.writelines(my_list)

with open('task2_2') as file_obj:
    lines = 0
    for line in file_obj:
        lines += 1
        letter = len(line) - 1
        print(letter)
    print(lines)


