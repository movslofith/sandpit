def f(a, b):
    """ returns sum of a, b"""
    return a + b

def g(a, b, c, d):
    """ returns sum of a, b, c, d"""
    return a + b + c + d
    

c = (4, 7)
d = (2, 3)

print(f(*c)) # must use asterix operator to unpack tuple

e = c + d

print(g(*e))

