def is_prime(n):
    """ Returns True when single integer argument is a prime number and False otherwise.
    """
    divisor = n - 1
    while divisor > 1:
        if n % divisor == 0:
            return False
        else:
            divisor -= 1
            continue
    return True

def primes_lessthan(n):
    """ Return list of all prime numbers less than n."""
    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)
    return result        
n = int(input("Gimme your number:"))
print("Here is a list of all the primes less than:", n, ":", primes_lessthan(n))

