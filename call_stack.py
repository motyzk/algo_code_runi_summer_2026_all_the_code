def foo(x):
    a = 5
    return max(a + x, 9)

def bar():
    l = [foo(9), 9]
    return sum(l)

print(bar())
