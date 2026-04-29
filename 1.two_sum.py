
class Solution:
    def twoSum(nums: [int], target: int) -> [int]:
        for i in range(len(nums)):
            if i <= len(nums):
                if nums[i] + nums[i+1] == target:
                    return[i, i+1]
        
        return nums

print(Solution.twoSum(nums=[3,2,3], target=6))