class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0: return []
        count_dict = {}

        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        count_key = {}
        for key,v in count_dict.items():
            if v in count_key:
                count_key[v].append(key)
            else:
                count_key[v] = [key]
        res = []
        for v in sorted(count_key.keys())[::-1]:
            if len(res) == k:
                return res
            for num in count_key[v]:
                if len(res) < k:
                    res.append(num)
                else:
                    return res
        return res

        