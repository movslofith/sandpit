def print_triangular_numbers(n):
    total = 0
    for i in range(n+1):
        total = total + i
    print(n, "\t", total)

print_triangular_numbers(1)
print_triangular_numbers(2)
print_triangular_numbers(3)
print_triangular_numbers(4)
print_triangular_numbers(5)
