class MyCalendarTwo:
    from heapq import heapify, heappop, heappush

    def __init__(self):
        # self.q = []
        # count = []
        # heapify(self.q)
        self.lst = []

    def book(self, start: int, end: int) -> bool:
        self.lst.append((start, +1))
        self.lst.append((end, -1))
        self.lst.sort()

        overbook = 0
        for l in self.lst:
            if overbook > 2:
                self.lst.remove((end, -1))
                return False
            overbook += l[-1]

        if overbook > 2:
            self.lst.remove((start, +1))
            self.lst.remove((end, -1))
            return False

        return True
