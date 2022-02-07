company = {'Ivanov': 21, 'Sidorov': 25, 'Izotova': 15, 'Dima': 30, 'Vika': 35, 'Arina': 17,
           'Anna': 13, 'Igor': 45, 'Artem': 16, 'Nikita': 27}

with open('task_3', 'w') as file_obj:
    for name, salary in company.items():
        file_obj.write(name + ' ' + str(salary) + '\n')

count = 0
summ = 0
staff = []
with open('task_3', 'r') as file_obj:
    for line in file_obj:
        my_line = line.split(' ')
        if int(my_line[1]) < 20:
            staff.append(my_line[0])
            summ += int(my_line[1])
            count += 1

profit = summ / count
print(staff)
print(profit)
