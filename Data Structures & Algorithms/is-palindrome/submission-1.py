class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        left = 0
        right = len(s) - 1
        def checkAlphanumeric(char):
            return ord('a') <= ord(char) <= ord('z') or ord('A') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9')

        while left < right:
            while left < right and not checkAlphanumeric(string[left]):
                left += 1
            while left < right and not checkAlphanumeric(string[right]):
                right -= 1
            if string[left] != string[right]:
                return False
            else:
                left += 1
                right -= 1

        return True