import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # leverage min-heap, based on points that have the smallest distance from (0,0) ensure it only has a size of k
        # we define the Euclidean distance function, call it on each points x and y, the return value is what is
        # pushed unto our min-heap in the form of (euclidean distance, coordinate)
        # after we fully populated our min-heap, we can pop from our min-heap k times and insert what is stored in
        # the second position of the tuple we're popping from our min-heap
        # return the list

        # initialize an empty list
        output = []

        # initialize an empty heap
        min_heap = []

        # for point in points
        for point in points:
            # call the Euclidean distance function on point
            dist = self.euclideanDistance(point[0], point[1])
            # push to queue 2-tuple = (result of Euclidean distance function, point)
            heapq.heappush(min_heap, (dist, point))
        
        # for k times
        for j in range(k):
            # pop from queue
            point = heapq.heappop(min_heap)
            # for our popped point, we insert 2-tuple in index 1 to our output list
            output.append(point[1])
        
        return output

    # defined Eucliean distance function
    def euclideanDistance(self, x, y):
        return math.sqrt(math.pow(x - 0, 2) + math.pow(y - 0, 2))

