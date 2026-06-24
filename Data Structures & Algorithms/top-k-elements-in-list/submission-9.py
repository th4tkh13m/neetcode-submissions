class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the freq -> dict
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        min_heap = []
        heapq.heapify(min_heap)

        for num, freq in freq_map.items():
            print(min_heap)
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        print(min_heap)
        return [num for _, num in min_heap]
