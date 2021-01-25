from unit_tester import test

def merge(xs, ys):
    """ Returns sorted list zs from merging sorted lists xs and ys
    """
    zs = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            zs.extend(ys[yi:])
            return zs
        
        if yi >= len(ys):
            zs.extend(xs[xi:])
            return zs
        
        if xs[xi] <= ys[yi]:
            zs.append(xs[xi])
            xi += 1
        else:
            zs.append(ys[yi])
            yi += 1

xs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
ys = [4, 8, 12, 16, 20, 24]
zs = xs + ys
zs.sort()

test(merge(xs, []) == xs)
test(merge([], ys) == ys)
test(merge([], []) == [])
test(merge(xs, ys) == zs)
test(merge([1,2,3], [3,4,5]) == [1,2,3,3,4,5])
test(merge(["a", "big", "cat"], ["big", "bite", "dog"]) == ["a", "big", "big", "bite", "cat", "dog"])