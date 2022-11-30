# factorial function 阶乘
def factorial(n):
    from math import prod
    return prod(range(1, n + 1))


def factorial_recursion(n):
    # 1. 找到终止递归的条件
    if 0 < n <= 2:
        return n
    # 1.找到f(n) 与 f(n - 1)的关系
    #  f(n) = f(n - 1) * n
    else:
        return n * factorial_recursion(n - 1)

# print(factorial_recursion(1002))   # default max recursion depth 1000

# get the complete path of all the folders and files in a given directory
import os

def getAllFilesRecursion(dir):
    allFolderAndFiles = []
    # base, folders, files, _ = os.walk(dir)
    # print(base, folders, files)
    print(gen:=os.walk(dir))
    for i in list(gen)[2]:
        print(i)
    print(len(list(gen)[1]))
# getAllFilesRecursion('E:/pystudy/python-notebooks')
