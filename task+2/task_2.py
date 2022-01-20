time_in_sec = input('Введите время в секундах в формате чч:мм:сс: ')

minute = time_in_sec.find(':')
sec = time_in_sec.find(':', minute + 1)

user_hour = int(time_in_sec[:minute]) // 3600
user_minute = int(time_in_sec[minute + 1:sec]) // 60
user_sec = int(time_in_sec[sec + 1:])

result = f'Время {user_hour:02}:{user_minute}:{user_sec}'

print(result)
