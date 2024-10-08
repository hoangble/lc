class Solution:
    from collections import Counter

    def removeDuplicateLetters(self, s: str) -> str:
        # counter number of letter in s
        # sort counter alphabetically -> O(1) for space
        # greedily remove letter from the top position
        last_occurrence = {c: i for i, c in enumerate(s)}
        seen = set()
        stack = []
        for i, s_ in enumerate(s):
            if s_ not in seen:
                while stack and stack[-1] > s_ and i < last_occurrence[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(s_)
                stack.append(s_)

        return "".join(stack)
