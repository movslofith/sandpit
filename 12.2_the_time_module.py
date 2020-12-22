import time

def do_my_sum(xs):
    sum = 0
    for v in xs:
        sum += v
    return sum

sz = 1000000
testdata = range(sz)

t0 = time.time()
my_result = do_my_sum(testdata)
t1 = time.time()
print("my_result = {0} (time taken = {1:.4f} seconds)".format(my_result, t1-t0))

t2 = time.time()
their_result = sum(testdata)
t3 = time.time()
print("their_result = {0} (time taken = {1:.4f} seconds)".format(their_result, t3-t2))
percent = (((t1 - t0)- (t3 - t2)) / (t3 - t2)) * 100
print("their_result was {0}% faster than my_result".format(percent))