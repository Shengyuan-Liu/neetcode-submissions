class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            left_v, mid_v, right_v = nums[left], nums[mid], nums[right]
            if mid_v == target:
                return mid
    
            if left_v <= mid_v:  # left is ordered
                if target >= left_v and target < mid_v:
                    right = mid - 1
                else:
                    left = mid + 1
            else:                # right is ordered
                if target > mid_v and target <= right_v:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
