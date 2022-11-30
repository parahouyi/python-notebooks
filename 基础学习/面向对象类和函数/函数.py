import functools


def testsum(a, b, c, d):
    print(a + b + c + d)


new_testsum = functools.partial(testsum, c=5, d=10)
new_testsum(1, 2)
new_testsum(1, 32)

assert 2>0, 'not true'
