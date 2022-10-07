# divide and conquer problem
# This problem was asked by Google.

# Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

# Do this faster than the naive method of repeated multiplication.

# For example, pow(2, 10) should return 1024

import timeit

dyn = '''
def pow_dynamic_programming(base = 2, power = 50, hash_map={}):
    # base case
    if power == 1:
        hash_map[1] = base
        return hash_map[1]
    elif power == 0:
        hash_map[0] = 1
        return hash_map[0]

    if power in hash_map:
        return hash_map[power]
    else:
        if power % 2 == 0:
            hash_map[power] = pow_dynamic_programming(
                base, power // 2, hash_map=hash_map) * pow_dynamic_programming(
                    base, power // 2, hash_map=hash_map)
            return hash_map[power]
        else:
            hash_map[power] = base * pow_dynamic_programming(
                base, (power - 1) // 2) * pow_dynamic_programming(
                    base, (power - 1) // 2)
        return hash_map[power]

'''

rec = '''
def pow_recursive(base = 2, power = 50):
    # base case
    if power == 1:
        return base
    elif power == 0:
        return 1

    if power % 2 == 0:
        return pow_recursive(base, power // 2) * pow_recursive(
            base, power // 2)
    else:
        return pow_recursive(base,
                                     (power - 1) // 2) * pow_recursive(
                                         base, (power - 1) // 2)
'''

print(timeit.timeit(dyn, number=1000))
print(timeit.timeit(rec, number=1000))
