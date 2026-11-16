class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = reversed(sorted(zip(position, speed), key=lambda x: x[0]))
        stack = []
        for p, s in position_speed:
            need_time = (target - p) / s
            if not stack:
                stack.append((p, s, need_time))
            else:
                if need_time > stack[-1][2]:
                    stack.append((p, s, need_time))
            # print(stack)
        return len(stack)


# [(1, 3), (4, 2)]


# [(0, 1), (1, 2), (4, 2), (7, 1)]

# (0, 1, 10)

# (1, 2, 4.5)

# (7, 1, 3)