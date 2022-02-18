import random

my_list = []

while len(my_list) < 10:
    i = str(random.randint(0, 100))
    my_list.append(i)

print(my_list)

with open('task_5.txt', 'w') as file_obj:
    file_obj.writelines(my_list)

