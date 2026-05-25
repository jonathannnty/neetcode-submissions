import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # priority queue as a possible optimal solution
        # we can use python's min-heap to find the two heaviest stones quickly (use as max-heap)
        # heapify our stones list

        # we repeat the following process until size of heap <= 1:
        # pop two stones from our heap and compare their values
        # if stone 1 == stone 2, do nothing to our heap
        # if stone 1 != stone 2, add the difference back into the heap
        # return size of our heap
        heapq.heapify_max(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            if stone1 != stone2:
                heapq.heappush_max(stones, abs(stone1 - stone2))
        return 0 if len(stones) == 0 else stones[0]
    