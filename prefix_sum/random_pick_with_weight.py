class BruteForceSolution:

    def __init__(self, w: List[int]):
        # self.prob = [i/w.sum() for i in w]
        self.w = w
        import time
        seed = int(time.time())
        # duplicate each item by the weight
        self.duplicated_arr = []
        for num, weight in enumerate(w):
            self.duplicated_arr += [num]*weight
        self.max_ = len(self.duplicated_arr)-1
        self.prev = seed
        
    def rng(self, prev):
        a = 11
        b = 15
        res =  (a*prev + b)%(self.max_ -0 + 1) + 0
        return res
    
    def pickIndex(self) -> int:
        idx = self.rng(self.prev)
        self.prev = idx
        return  self.duplicated_arr[idx]
