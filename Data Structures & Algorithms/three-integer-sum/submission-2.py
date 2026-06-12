class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_arr = sorted(nums)
        start, end = 0, len(nums) - 1
        result_list = []

        while start < end:
            # 2 Sums in the middle
            middle = start + 1
            right = end
            while middle < right:
                if sorted_arr[middle] + sorted_arr[right] < - sorted_arr[start]:
                    middle += 1
                elif sorted_arr[middle] + sorted_arr[right] == - sorted_arr[start]:
                    result_list.append([sorted_arr[start], sorted_arr[middle], sorted_arr[right]])
                    right -= 1
                    middle += 1
                    while right > -1 and sorted_arr[right] == sorted_arr[right + 1]  :
                        right -= 1
                else:
                    right -= 1

            start += 1
            while start < len(nums) and sorted_arr[start] == sorted_arr[start - 1]  :
                start += 1



        return result_list
                