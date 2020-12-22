def range(n):
    return 123*n

print(range(10))

n = 10
m = 3
def f(n):
    m = 7
    return 2 * n + m

print(f(5), n, m)