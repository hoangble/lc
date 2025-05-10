def strStr(haystack: str, needle: str) -> int:
    i = 0
    n = len(haystack)
    j = 0
    m = len(needle)

    while i < n:
        if haystack[i] == needle[j]:
            j += 1
        else:
            j = 0
        # print(i, haystack[i], j, needle[j])
        i += 1

        if j == m:
            return i - m

    return -1


strStr("mississippi", "issip")
