# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        x=len(nums)
        ans = []
        for i in range(1<<x):
            ans.append([nums[j] for j in range(x) if i&(1<<j)])
        return ans
        
