def sqrt(n):
    approx = n/2.0
    iteration = 1
    while True:
        better = (approx + n/approx)/2.0            
        print("The output of iteration", iteration, "is", better)
        if abs(approx - better) < 0.000001:
            return better
        approx = better 
        iteration += 1

print(sqrt(25.0))
print(sqrt(49.0))
print(sqrt(81.0))

