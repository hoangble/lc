from typing import List 

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        # buses.sort()
        # passengers.sort()
        # n = len(passengers)

        # # find the bus with 
        # curr = 0
        # for time in buses:
        #     cap = capacity
        #     while cap > 0 and curr < n and passengers[curr] <= time:
        #         cap -= 1
        #         curr += 1
        
        # best = time if cap > 0 else passengers[curr - 1]
        # while best in set(passengers):
        #     best -= 1
        # return best
        
        buses.sort()
        passengers.sort()

        curr = 0
        prev = -1
        for i in range(len(buses)):
            cap = 0
            while cap < capacity and curr < len(passengers) and passengers[curr] <= buses[i]:
                if passengers[curr] - 1 ==  prev:
                    ans = passengers[curr] - 1
                prev = passengers[curr]
                curr += 1
                cap += 1
            if cap < capacity and buses[i] != prev:
                ans = buses[i]

        return ans