from typing import List
from builtins import int


class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        i = 0
        j = 0
        nums1_length = len(nums1)
        nums2_length = len(nums2)
        merged_nums = []
        # Merge elements of two list in ascending order.
        while (i < nums1_length and j < nums2_length):
            if (nums1[i] < nums2[j]):
                merged_nums.append(nums1[i])
                i += 1
            else:
                merged_nums.append(nums2[j])
                j += 1

        # print(str(i) + ":" + str(j))
        # print(*merged_nums, sep=',')
        # # Add remaining elements of nums1/nums2 to merged array.
        while (i < nums1_length):
            merged_nums.append(nums1[i])
            i += 1
        while (j < nums2_length):
            merged_nums.append(nums2[j])
            j += 1

        # print(*merged_nums, sep='|')

        merged_nums_len = len(merged_nums)
        median_base_index = int((merged_nums_len - 1) / 2)
        if merged_nums_len % 2 != 0:
            median = float(merged_nums[median_base_index])
        else:
            median = float((merged_nums[median_base_index] + merged_nums[median_base_index + 1]) / 2)

        return median


nums_lists = []
for _ in range(2):
    # Get input and remove any white spaces at the end of the string.
    input_str = input().rstrip()
    nums = list(map(int, input_str.split(' ')))
    nums_lists.append(nums)


solution = Solution()
median = solution.findMedianSortedArrays(nums1=nums_lists[0], nums2=nums_lists[1])
print(median)
