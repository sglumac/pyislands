from itertools import izip


def geom(x0, q, xmax):
    x = x0
    while x < xmax:
        yield x
        x *= q

def bottom_up_merge(xs, ys, ileft, iright, iend):
    i0 = ileft
    i1 = iright
    num_inversions = 0
    for j in xrange(ileft, iend):
        if i0 < iright and (i1 >= iend or xs[i0] <= xs[i1]):
            ys[j] = xs[i0]
            i0 += 1
        else:
            ys[j] = xs[i1]
            i1 += 1
            num_inversions += iright - i0
    return num_inversions


def bottom_up_sort(xs):
    n = len(xs)
    ys = list(xs)
    tmp = range(n)
    inv = 0
    for width in geom(1, 2, n):
        for ileft in xrange(0, n, 2 * width):
            iright = min(ileft + width, n)
            iend = min(ileft + 2 * width, n)
            inv += bottom_up_merge(ys, tmp, ileft, iright, iend)

        ys, tmp = tmp, ys

    return ys, inv


def inversions_on2(xs):
    n = len(xs)
    inv = 0
    for i in range(n):
        for j in range(i + 1, n):
            inv += xs[i] > xs[j]
    return inv

def distance(px, py):
    '''
    distance between two permutations px and py,
    measured as a number of inversions of px * py^-1
    '''

# inverse - ipy = py^-1
    #import ipdb; ipdb.set_trace() # BREAKPOINT
    _, ipy = izip(*sorted((e, i) for i, e in enumerate(py)))
# apply px to inverse - pr = px * ipy
    pr = [px[i] for i in ipy]

    _, inversions = bottom_up_sort(pr)

    return inversions


def main():
    n = 1000
    xs = range(n)
    import random
    random.shuffle(xs)
    print xs
    inv = inversions_on2(xs)
    print "real inv =", inv
    ys, inv = bottom_up_sort(xs)
    print ys
    print "xs is sorted =", ys == range(n)
    print "inversions =", inv


if __name__ == '__main__':
    main()
