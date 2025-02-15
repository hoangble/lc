from threading import Lock
class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k   
        self.q = [None] * k
        self.head_idx = 0
        self.cnt = 0
        self.q_lock = Lock()

    def enQueue(self, value: int) -> bool:
        with self.q_lock:
            if self.cnt == self.k: return False 

            new_idx = (self.head_idx + self.cnt) % self.k 
            self.q[new_idx] = value
            self.cnt += 1
        return True
        

    def deQueue(self) -> bool:
        if self.cnt == 0: return False 

        self.head_idx = (self.head_idx + 1) % self.k
        self.cnt -= 1
        return True

    def Front(self) -> int:
        if self.cnt == 0: return -1

        return self.q[self.head_idx]

    def Rear(self) -> int:
        if self.cnt == 0: return -1
        return self.q[(self.head_idx + self.cnt - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.cnt == 0

    def isFull(self) -> bool:
        return self.k == self.cnt


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()