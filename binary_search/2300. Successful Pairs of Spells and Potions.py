def binary_search(a, t) -> int:
    l, r = 0, len(a) - 1
    while l <= r and l >= 0:
        m = (l + r) // 2
        if a[m] == t:
            return m

        if a[m] > t:
            r = m - 1
        else:
            l = m + 1

    print(l, r)
    if a[r] >= t:
        return r
    else:
        return max(l, 0)


# a = [5,10,15,20,25]
a = sorted([38, 36, 23])
t = 328 / 15

print(binary_search(a, t))
