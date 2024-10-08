class Solution():
    def minLength(self, string: str) -> int:
        stack = []
        for _s in string:
            if not stack:
                stack.append(_s)
            else:
                match _s:
                    case "B":
                        if stack[-1] == "A":
                            stack.pop()
                        else:
                            stack.append(_s)
                    case "D":
                        if stack[-1] == "C":
                            stack.pop()
                        else:
                            stack.append(_s)
                    case _:
                        stack.append(_s)
        return len(stack)

sol = Solution()
sol.minLength('ABFCACDB')
