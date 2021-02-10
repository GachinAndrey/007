class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):

        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.my_list]))

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)


m = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
new_m = Matrix([[31, 22, 3], [37, 43, 5], [51, 86, 8]])
print(m.__add__(new_m))
