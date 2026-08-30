# O(n) time, O(n) space
def solve(n):
    arr = list(range(1, n+1))
    while len(arr) != 1:
        arr = arr[1::2]
        arr.reverse()
    return arr.pop()


# O(n) time, O(n) space
def solve(n):
    arr = list(range(1, n + 1))
    start_to_end = True
    while len(arr) != 1:
        slice_from = 1 if len(arr) % 2 == 1 or start_to_end else 0
        arr = arr[slice_from::2]
        start_to_end = not start_to_end
    return arr.pop()


# O(log(n)) time, O(log(n)) space
def solve(n):
    def rec(n, left_to_right):
        if n == 1:
            return n
        if left_to_right:
            return 2 * rec(n // 2, False)
        if n % 2 == 1:
            return 2 * rec(n // 2, True)
        return 2 * rec(n // 2, True) - 1
    return rec(n, True)
# def solve(n, left_to_right=True):
#     if n == 1:
#         return n
#     if left_to_right:
#         return 2 * solve(n // 2, False)
#     if n % 2 == 1:
#         return 2 * solve(n // 2, True)
#     return 2 * solve(n // 2, True) - 1


from collections import deque
def solve(n):
    stacks = [deque(reversed(range(1, n+1))), deque()]
    curr_full_stack = 0
    while True:
        if len(stacks[0]) == 1 or len(stacks[1]) == 1:
            non_empty_stack = stacks[0] or stacks[1]
            return non_empty_stack.pop()
        curr_empty_stack = 1 - curr_full_stack
        while stacks[curr_full_stack]:
            stacks[curr_full_stack].pop()
            if stacks[curr_full_stack]:
                stacks[curr_empty_stack].append(
                    stacks[curr_full_stack].pop())
        curr_full_stack = 1 - curr_full_stack


assert solve(9) == 6
assert solve(1) == 1
