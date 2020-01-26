"""
Input an integer n and outputs a list with 1 once, 2 twice, 3 three times….n ntimes e.g. f(3) = [1,2,2,3,3,3]
"""


def counter(num):
    return [i for i in range(1, num+1) for _ in range(i)]


def counter_2(num):
    l = []
    for i in range(1, num+1):
        l.extend([i] * i)
    return l


print(counter_2(3))



d = set([1,2, 3])
l = {}

l[("ahmed", "mohamed")] = 10
print(d)
print(l)