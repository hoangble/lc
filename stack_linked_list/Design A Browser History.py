# https://leetcode.com/problems/design-browser-history/description/
# 1472. Design Browser History


class BrowserHistory:
    def __init__(self, homepage: str):
        self.stack = [homepage]  # double linked-list actually
        self.pointer = 0

    def visit(self, url: str) -> None:
        while len(self.stack) != self.pointer + 1:
            # remove all history for forwards, so forward till the current index
            self.stack.pop()
        self.stack.append(url)
        self.pointer += 1

    def back(self, steps: int) -> str:
        self.pointer = self.pointer - steps
        self.pointer = 0 if self.pointer < 0 else self.pointer
        return self.stack[self.pointer]

    def forward(self, steps: int) -> str:
        self.pointer = self.pointer + steps
        self.pointer = (
            len(self.stack) - 1 if self.pointer >= len(self.stack) else self.pointer
        )
        return self.stack[self.pointer]
