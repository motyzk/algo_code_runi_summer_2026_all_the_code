# TODO naive approach O(n**2) time


# O(n) space and time
def solve(l):
    ans = [-1] * len(l)
    stack = []
    for i in reversed(range(len(l))):
        while stack and stack[-1] <= l[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(l[i])
    return ans


assert solve([2, 1, 2, 3, 4]) == [3, 2, 3, 4, -1]
assert solve([2]) == [-1]
assert solve([]) == []
