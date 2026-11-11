class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = len(nums)
        return not(l == len(set(nums)))