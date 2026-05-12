# 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i - 1]):
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                res = nums[i] + nums[l] + nums[r]
                if res == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < len(nums) - 1 and nums[l] == nums[l + 1]:
                        l += 1
                    while r > 0 and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif res < 0:
                    l += 1
                else:
                    r -= 1

        return result
