class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in table:
                return [table[difference], i]
            else:
                table[nums[i]] = i