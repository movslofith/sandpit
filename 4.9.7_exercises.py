def sum_to(n):
    """
    Returns the sum of all integer numbers up to and including n.
    """
    sum = 0
    for i in range(n+1):
        sum = sum + i
    
    return sum
10
n = int(input("What number would you like to sum all the numbers up to? "))

print("The sum of all the numbers up to", n, "is", sum_to(n))