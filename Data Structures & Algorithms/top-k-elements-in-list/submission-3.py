class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # output init elements meant to indicate that we 
        # haven't determined most freq elements just yet
        output = [-1001] * k

        # set up hashmap to count frequencies
        hashmap = {}
        for num in nums:
            print(num)
            print(f"output: {output}")
            if num not in hashmap.keys():
                print("num is not hashmap")
                hashmap[num] = 1
                for idx in range(len(output)):
                    if output[idx] == -1001:
                        output[idx] = num
                        break
            # num exists in our freq hashmap
            else:
                print("num is in hashmap")
                hashmap[num] += 1
                if num not in output:
                    for idx in range(len(output)):
                        # if output[idx] == -1001, then we know that
                        # we have yet to encounter another unique character
                        # to populate
                        if output[idx] == -1001:
                            break
                        if hashmap[num] > hashmap[output[idx]] and num != output[0]:
                            output[idx] = num
                            break
        return output