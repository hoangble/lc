from heapq import heapify, heappop, heappush


class MaxStack:
    def __init__(self):
        self.stack = []
        self.soft_delete = set()
        self.max_heap = []
        heapify(self.max_heap)
        self.idx = 0

    def _clean_up_stack(self):
        while self.stack and self.stack[-1][-1] in self.soft_delete:
            self.soft_delete.remove(self.stack.pop()[-1])

    def _clean_up_heap(self):
        while self.max_heap and self.max_heap[0][-1] in self.soft_delete:
            self.soft_delete.remove(heappop(self.max_heap)[-1])

    def push(self, x: int) -> None:
        self.stack.append((x, self.idx))
        heappush(self.max_heap, (-x, self.idx))
        self.idx -= 1

    def pop(self) -> int:
        self._clean_up_stack()
        last_push = self.stack.pop()
        self.soft_delete.add(last_push[-1])
        return last_push[0]

    def top(self) -> int:
        self._clean_up_stack()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        self._clean_up_heap()
        return self.max_heap[0][0] * -1

    def popMax(self) -> int:
        self._clean_up_heap()
        curr_max = heappop(self.max_heap)
        self.soft_delete.add(curr_max[-1])
        return curr_max[0] * -1


# Your MaxStack object will be instantiated and called as such:
obj = MaxStack()
obj.push(5)
obj.push(1)
obj.push(5)

print(obj.top())
print(obj.popMax())
print(obj.top())

print(obj.peekMax())
print(obj.pop())
print(obj.top())
