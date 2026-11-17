class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]: return nums[left]
        while left < right:
            mid = (left + right) // 2
            left_v, mid_v, right_v = nums[left], nums[mid], nums[right]
            if mid_v > right_v:
                left = mid + 1
            else:
                right = mid
        return nums[left]