class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for i in range(len(temperatures))]
        for i, num in enumerate(temperatures):
            if not stack:
                stack.append((i, num))
            else:
                while stack and stack[-1][1] < num:
                    smaller_i, smaller_num = stack.pop()
                    result[smaller_i] = i - smaller_i
                stack.append((i, num))
            # print(stack)
        return result