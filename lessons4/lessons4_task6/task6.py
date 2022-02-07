from itertools import cycle, count

for el in count(3):
    print(el)
    if el == 10:
        break

i = 0
my_list = [1, 3, 5, 7, 8, 10]

for el in cycle(my_list):
    print(el)
    i += 1
    if i == 55:
        break
