import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # brute/naive approach sort > sorted(nums)[len(nums) - k]
        # runtime: o(nlogn) log-linear

        # max-heap for nums
        # the kth operation of popping from this max-heap after populating it

        # initialize an empty max-heap
        max_heap = []

        # for num in nums
        for num in nums:
            # push unto this max-heap the num
            heapq.heappush_max(max_heap, num)
        
        # for 1 to k - 1
        for j in range(k - 1):
            # pop for the max-heap
            heapq.heappop_max(max_heap)
        
        # return the last pop operation
        return heapq.heappop_max(max_heap)