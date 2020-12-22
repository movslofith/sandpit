import copy
a = [1, 1, 1]
b = [2, 2, 2]

x = [a, b]
y = copy.copy(x)
z = copy.deepcopy(x)

print(x, y, z)

a = [3, 3, 3]

print(x, y, z)
