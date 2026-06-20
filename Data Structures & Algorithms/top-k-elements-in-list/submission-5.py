class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # key idea: hashmap integer -> count
        # keep track of the count
        
        val_to_count = {}

        for val in nums:
            if not val in val_to_count:
                val_to_count[val] = 1
            else:
                val_to_count[val] += 1
        
        # What we can do: min heap, push the min out when heap > k
        heap = []
        for num in val_to_count.keys():
            heapq.heappush(heap, (val_to_count[num], num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
    