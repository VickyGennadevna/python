def my_fact(num):
    count = 1
    while count <= num:
        yield count
        count += 1

i = 1
for el in my_fact(5):
    i = i * el

print(i)