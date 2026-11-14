class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left_max = 0
        left_max_array = [0 for i in range(n)]
        right_max = 0
        right_max_array = [0 for i in range(n)]
        for i in range(n):
            left_max_array[i] = left_max
            left_max = max(left_max, height[i])
        for i in range(n - 1, -1, -1):
            right_max_array[i] = right_max
            right_max = max(right_max, height[i])
        
        capacity = 0
        for i in range(n):
            capacity += max(0, min(left_max_array[i], right_max_array[i]) - height[i])
        return capacity