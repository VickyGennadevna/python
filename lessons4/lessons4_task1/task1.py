from sys import argv

print(argv)

work_hours = int(argv[1])
salary_in_hour = int(argv[2])
bonus = int(argv[3])

result = f'Summa = {work_hours * salary_in_hour + bonus}'
print(result)

