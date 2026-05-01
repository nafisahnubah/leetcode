# Two Sum
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.
#
# Example 1:
# Input: nums = [3,4,5,6], target = 7
# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].
#
# Example 2:
# Input: nums = [4,5,6], target = 10
# Output: [0,2]
#
# Example 3:
# Input: nums = [5,5], target = 10
# Output: [0,1]
#
# Constraints:
# 2 <= nums.length <= 1000
# -10,000,000 <= nums[i] <= 10,000,000
# -10,000,000 <= target <= 10,000,000
# Only one valid answer exists.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_nums = nums.copy()
        nums.sort()
        i = 0
        j = len(nums)-1
        while(i<j):
            temp = nums[i] + nums[j]
            if(temp==target):
                if(temp_nums.index(nums[i], 0, len(nums))==temp_nums.index(nums[j], 0, len(nums))):
                    arr = [temp_nums.index(nums[i], 0, len(nums)), temp_nums.index(nums[j], temp_nums.index(nums[i], 0, len(nums))+1, len(nums))]
                else:
                    arr = [temp_nums.index(nums[i], 0, len(nums)), temp_nums.index(nums[j], 0, len(nums))]
                return sorted(arr)
            elif(temp>target):
                j = j-1
            else:
                i = i+1