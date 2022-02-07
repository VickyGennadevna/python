my_list1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

my_list2 = [el for el in my_list1 if el > my_list1[my_list1.index(el) - 1]]

print(my_list2)

