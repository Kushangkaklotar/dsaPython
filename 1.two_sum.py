
class Solution:
    def twoSum(nums: [int], target: int) -> [int]:

        for i in range(len(nums)):
            if i >= range(len(nums)):
                if nums[i] + nums[i+1] == target:
                    return[nums[i], nums[i+1]]
        
        return nums

print(Solution.twoSum(nums=[2,7,11,15], target=9))