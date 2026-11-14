class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:   # 去重:跳过相同的 nums[i]
                continue
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1                        # 不 return,继续找
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:    # 去重
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:  # 去重
                        right -= 1
        return result