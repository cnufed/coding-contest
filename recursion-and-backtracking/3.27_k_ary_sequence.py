from pprint import pprint


def append(x, L):
    return [x + elem for elem in L]


def k_ary_sequence(n, k):
    if n == 0:
        return []
    elif n == 1:
        return (str(d) for d in range(0, k))
    else:
        return [str(d) + s for d in range(0, k) for s in k_ary_sequence(n - 1, k)]


# This algorithm is under the backtracking category.
# The time complexity is O(k^n)
pprint(k_ary_sequence(3, 3))
