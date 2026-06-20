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
        
        # What we can do: count -> val, sort, take top k
        count_to_val = [(c,v) for v, c in val_to_count.items()]
        
        sorted_keys = sorted(count_to_val, reverse=True)
        result = [v for c, v in sorted_keys[:k]]
        
        return result
    