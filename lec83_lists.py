checked_list = [1, 2, 3, 4]
print(8 not in checked_list)

indexes_ex = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 0]]
print(indexes_ex[2][0])
print(indexes_ex[-1])

slicing = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(slicing[:4])
slicing[3] = -20
print(slicing)
slicing[8:10] = [100, 100, 100]
print(slicing)
slicing.insert(1, "turtle")
print(slicing)
print(slicing.index(60))
print(checked_list.pop())

import copy
ex_12 = copy.deepcopy(slicing)
ex_12[1] = 40
print(ex_12)
