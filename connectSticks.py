def connectSticks(self, sticks):
    res = 0
    heapq.heapify(sticks)
    while len(sticks) > 1:
        c = heapq.heappop(sticks)+heapq.heappop(sticks)
        res += c
        heapq.heappush(sticks,c)
    return res
