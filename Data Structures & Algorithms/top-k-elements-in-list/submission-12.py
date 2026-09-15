class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Idea: get the frequency into a dict
        # Sort by frequency then get top k

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        

        # Resort freq
        sorted_freq = sorted([(v, k) for k, v in freq.items()], reverse=True)
        result = []
        for count in range(k):
            result.append(sorted_freq[count][1])
        return result


        # # We can sort by the (v, k) using heap
        # from heapq import heappop, heappush, heapify

        # h = []
        # heapify(h)
        # for key, v in freq.items():
        #     heappush(h, (-v, key))
        # result = []
        # for count in k:
        #     result.p(h[])
