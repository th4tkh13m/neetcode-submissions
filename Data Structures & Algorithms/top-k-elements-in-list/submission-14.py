class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}

        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        
        sorted_keys = sorted(num_count.keys(), key=lambda x: num_count[x], reverse=True)
        return list(sorted_keys)[:k]