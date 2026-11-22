class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Sort by count
        count_map = {}

        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
        
        sorted_keys = sorted(count_map, key=lambda x: count_map[x], reverse=True)
        return sorted_keys[:k]