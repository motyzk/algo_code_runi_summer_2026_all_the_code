l = [0, 1, 2, 3]

for n in l:
    n = 10

print(l)

for i in range(len(l)):
    l[i] = 10

print(l)


# --------------------------------
# call by value vs by reference

n = 8

def func(num):
    num = 90
    print(num)

func(n)

print(n)


l = [0, 1, 2, 3, 4]

def func2(nums):
    for n in nums:
        n = 90
func2(l)
print(l)

def func2(nums):
    for i in range(len(nums)):
        nums[i] = 90
func2(l)
print(l)
