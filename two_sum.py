# https://leetcode.com/problems/two-sum/


class Solution(object):
    def twoSum(self, nums: list, target: int) -> list[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        l_n = len(nums)

        for i in range(l_n):
            for j in range(l_n):
                if j != i:
                    if nums[i] + nums[j] == target:
                        return [i, j]

        return [None]


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))
