class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        nums = self.data.get(key, [])
        if not nums: return ""
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid][0] == timestamp:
                return nums[mid][1]
            
            if nums[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid
        return nums[left][1] if nums[left][0] <= timestamp else ""