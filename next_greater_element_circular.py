# TODO naive approach O(n**2) time


# O(n) space and time
def solve(l):
    ans = [-1] * len(l)
    stack = []
    for i in (range(2 * len(l) - 1, -1, -1)):
        while stack and stack[-1] <= l[i % len(l)]:
            stack.pop()
        if stack:
            ans[i % len(l)] = stack[-1]
        stack.append(l[i % len(l)])
    return ans


assert solve([2, 1, 2, 3, 4]) == [3, 2, 3, 4, -1]
assert solve([1, 2, 1]) == [2, -1, 2]
assert solve([2]) == [-1]
assert solve([]) == []
