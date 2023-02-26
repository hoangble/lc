class MedianFinder: 
    from heapq import heappush, heappop, heapify
    def __init__(self):
        self.max_heap = []
        heapify(self.max_heap)
        self.min_heap = []
        heapify(self.min_heap)
        

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0: 
            heappush(self.min_heap, num)
            return
        
        # if len(self.max_heap) == 0: 
        #     heappush(self.max_heap, num*-1)

        if num > self.min_heap[0]:
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, num*-1)

        if len(self.max_heap) < len(self.min_heap) - 1:
            heappush(self.max_heap, heappop(self.min_heap) * -1)
        # print(self.max_heap, self.min_heap)

        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, heappop(self.max_heap) * -1)
        return

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.max_heap[0]*-1 + self.min_heap[0]) /2
        else:
            return self.min_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
