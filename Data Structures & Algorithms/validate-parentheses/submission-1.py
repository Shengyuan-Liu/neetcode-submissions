class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        right_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        left = set(['(', '{', '['])
        for char in s:
            if char in left:
                stack.append(char)
            else:
                if not stack or stack[-1] != right_map[char]:
                    return False
                else:
                    stack.pop()
        return True if not stack else False
