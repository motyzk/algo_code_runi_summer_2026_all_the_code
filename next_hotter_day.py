# TODO naive approach O(n**2) time


def solve(temps):
    ans = [0] * len(temps)
    stack = []
    for i in range(len(temps)-1, -1, -1):
        while stack and temps[stack[-1]] <= temps[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1] - i
        stack.append(i)
    return ans


assert solve([]) == []
assert solve([33]) == [0]
assert solve([33, 34, 35, 31, 29, 32, 36, 33]) == [1, 1, 4, 2, 1, 1, 0, 0]
