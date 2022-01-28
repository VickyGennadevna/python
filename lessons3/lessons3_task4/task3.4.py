#def my_func(x, y):
    #result = x ** y
    #return result

#my_result = my_func(5, -3)

#print(my_result)

def my_func(x, y):
    while y < 0:
        result = 1 / x * x
        y += 1
    return result

my_result = my_func(3, -3)
print(my_result)
