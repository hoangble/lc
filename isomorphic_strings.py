class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_dict = {}
        for i in range(len(s)):
            if s[i] not in char_dict.keys():
                if t[i] not in char_dict.values():
                    char_dict = {}
                else:
                    return False
            else:
                if char_dict[s[i]] != t[i]:
                    print(s[i], t[i])
                    return False
        return True


if __name__ == "__main__":
    sol = Solution()
    s = "foo"
    t = "bar"
    sol.isIsomorphic(s, t)
