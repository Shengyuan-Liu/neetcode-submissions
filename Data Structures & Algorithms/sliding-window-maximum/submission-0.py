class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        head = 0
        result = []

        for i, num in enumerate(nums):
            while len(q) > head and nums[q[-1]] < num:
                q.pop()
            q.append(i)

            if q[head] <= i - k:
                head += 1
            
            if i >= k - 1:
                result.append(nums[q[head]])

        return result