def print_multiples(n, low, high):
    for i in range(low, high):
        print(n * i, end="\t")
    print()

for j in range (1, 7):
    print_multiples(j, 1, 11)
