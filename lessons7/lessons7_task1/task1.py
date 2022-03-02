import copy


class Matrix:
    
    def __init__(self, matrix):
        self.matrix = matrix
        
    def __str__(self):
        res = ''
        for i in range(len(self.matrix)):
            res = res + '\t'.join(map(str, self.matrix[i])) + '\n'
        return res
    
    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        result = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                result[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(result)

my_list1 = [[2, 6, 7], [9, 8, 7], [1, 2, 3]]
my_list2 = [[1, 1, 1], [2, 3, 3], [12, 11, 12]]
add_list1 = Matrix(my_list1)
add_list2 = Matrix(my_list2)
print(add_list2)
add_result = add_list1 + add_list2
print(add_result)
        