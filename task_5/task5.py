revenue = int(input('Введите выручку вашей фирмы: '))
costs = int(input('Введите издержки вашей фирмы: '))

if revenue > costs:
    print('Вы в прибыли')
    profitability = (revenue - costs) / revenue
    staff = int(input('Введите численность сотрудников: '))
    staff_profit = profitability / staff
    print(staff_profit)

else:
    print('Вы в убытке')