my_numbers = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4}

with open('task_4.txt', 'w+') as file_obj:
    for number, value in my_numbers.items():
        file_obj.write(number + ' - ' + str(value) + '\n')

result = []
new_list = ['один', 'два', 'три', 'четыре']
count = 0
with open('task_4.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' - ')
        i[0] = new_list[count]
        result.append(i[0] + ' - ' + i[1])
        count += 1

with open('result_task.txt', 'w', encoding='utf-8') as file_obj2:
    file_obj2.writelines(result)

print(result)
