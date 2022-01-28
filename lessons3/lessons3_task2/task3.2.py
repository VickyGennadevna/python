def info_users(name, lastname, birth, city, user_email, user_phone):
    result_func = name, lastname, birth, city, user_email, user_phone
    return result_func



result = info_users(name = input('Введите имя: '), lastname = input('Введите фамилию: '),
birth = input('Год рождения: '), city = input('Ваш город проживания: '),
user_email = input('Введите ваш почтовой адрес: '), user_phone = input('Введите ваш номер телефона: '))

print(result)