class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # you want to iterate from right to left
        # initially set the last element to -1, but keep record of its original element
        # as you're iterating from right to left, if current element < what we've recorded
        # set current element to what we've recorded
        # OTHERWISE, if current element > what've recorded, we still assign it to what we've recorded
        # but we update our record as current element is now our greatest element

        record = arr[-1]
        arr[-1] = -1

        for idx in range(len(arr) - 2, -1, -1):
            if arr[idx] < record:
                arr[idx] = record
            else:
                arr[idx], record = record, arr[idx]
        return arr
