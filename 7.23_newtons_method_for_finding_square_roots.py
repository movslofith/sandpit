def sqrt(n):
    approx = n/2.0
    while True:
        better = (approx + n/approx)/2.0
        if abs(approx - better) < 0.000001:
            return better
        approx = better 

print(sqrt(25.0))
print(sqrt(49.0))
print(sqrt(81.0))

