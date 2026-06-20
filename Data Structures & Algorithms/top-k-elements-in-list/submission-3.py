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
        count_to_val = {}
        for v, c in val_to_count.items():
            if not c in count_to_val:
                count_to_val[c] = [v]
            else:
                count_to_val[c].append(v)
        # Sort 
        sorted_keys = sorted(list(count_to_val.keys()))
        result = []
        print(count_to_val)
        for count in sorted_keys[::-1]:
            for v in count_to_val[count] :
                if len(result) < k:
                    result.append(v)
        return result
    