class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        record = set()
        left, right = 0, 1
        record.add(s[left])
        length = 1
        max_length = 1
        while right < len(s):
            while s[right] in record:
                record.remove(s[left])
                left += 1
                length -= 1
            record.add(s[right])
            length += 1
            max_length = max(max_length, length)
            right += 1
        return max_length