def int_func(words):
    separate_userw = words.split()
    my_list = []
    for i in separate_userw:
        string_word = str(i)
        first_letter = i[0].upper()
        word = first_letter + string_word[1:]
        my_list.append(word)
    return my_list

result = int_func('text vika')
print(result)

