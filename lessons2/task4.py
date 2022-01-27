user_elems = input('ведите строку, разделенную пробелами: ').split()

for i, elem in enumerate(user_elems):
    print(i + 1, elem[:10])
