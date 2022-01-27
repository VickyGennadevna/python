user_count = int(input('Введите количество товаров: '))

n = 1
list_1 = []
my_dict = []


while n <= user_count:
    my_dict = {
        'name_product': input('Введите название товара: '), 'price': input('Введите цену товара: '),
        'quantity': input('Введите количество: '), 'unit': input('Единица измерения: ')
    }
    list_1.append((n, my_dict))
    n += 1

print(list_1)

analytics = {}
for list_ in list_1:
    for key, value in list_[1].items():
        if key in analytics:
            analytics[key].append(value)
        else:
            analytics[key] = [value]

#analytics = dict(
      #  {'name_product': my_dict.get('name_product'), 'price': my_dict.get('price'),
        #'quantity': my_dict.get('quantity'), 'unit': my_dict.get('unit')})


print(analytics)

