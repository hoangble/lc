class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_types = {")":"(", "}":"{", "]":"["}
        
        for s_ in s:
            if s_ == "(" or s_ == "{" or s_ == "[":
                stack.append(s_)
            else:
                if not stack or bracket_types[s_] != stack[-1]:
                    return False
                stack.pop()
        return not stack