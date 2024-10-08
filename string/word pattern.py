class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_tokens = s.split(" ")
        if len(s_tokens) != len(pattern):
            return False
        s_to_p = {}
        p_to_s = {}

        for p_token, s_token in zip(pattern, s_tokens):
            if s_token not in s_to_p:
                s_to_p[s_token] = p_token

            if p_token not in p_to_s:
                p_to_s[p_token] = s_token
            # print(s_to_p)
            # print(p_to_s)

            if s_to_p[s_token] != p_token or p_to_s[p_token] != s_token:
                return False

        return True
