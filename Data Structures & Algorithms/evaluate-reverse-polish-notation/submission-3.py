class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])
        for s in tokens:
            if s not in operators:
                stack.append(int(s))
            else:
                if s == '+':
                    result = stack[-2] + stack[-1]
                elif s == '-':
                    result = stack[-2] - stack[-1]
                elif s == '*':
                    result = stack[-2] * stack[-1]
                else:
                    sign = 1 if stack[-2] / stack[-1] > 0 else -1
                    result = sign * (abs(stack[-2]) // abs(stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(result)
            # print(stack)
        return stack[-1]