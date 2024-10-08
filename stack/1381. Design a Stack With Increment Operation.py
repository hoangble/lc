class CustomStack:
    # Push and pop are O(1), increment is O(n)
    def __init__(self, maxSize: int):
        self.max_size = maxSize

        self.l = 0  # first non zero element
        self.r = 0  # last non zero element

        self.stack = [-1] * self.max_size

    def push(self, x: int) -> None:
        # if right < max_size
        # if the left pointer is at 0 then move the right pointer 1 space to the right
        # else move the left pointer 1 space to the left
        if self.r == self.max_size - 1 and self.l == self.r:
            # if max_size = 1
            if self.stack[self.r] == -1:
                self.stack[self.r] = x
            return

        if self.r < self.max_size:
            if self.l == 0:
                self.stack[self.l] = x
                self.r += 1
            else:
                self.l -= 1
                self.stack[self.l] = x

    def pop(self) -> int:
        # pop self.stack[self.left]
        # if l == r, return the current l, and set it to -1
        # else l -= 1

        if self.l >= 0:
            to_return = self.stack[self.l]
            self.l += 1

        if self.l == self.r:
            self.l = self.r = 0

        return to_return

    def increment(self, k: int, val: int) -> None:
        # for i in min(l to r) or k: increment all elements by val
        # if l == r, self.stack[i] == -1 then don't do anything
        total_space = self.r - self.l
        if total_space > 0:
            if total_space > k:
                total_space = k

            for i in range(self.r - 1, self.r - total_space - 1, -1):
                print(i)
                self.stack[i] += val
        else:
            if self.stack[0] != -1:
                self.stack[0] += val
