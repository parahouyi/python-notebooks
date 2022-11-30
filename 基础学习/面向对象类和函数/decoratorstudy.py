# def outer():
#     x = 1
#
#     def inner(*args,**kwargs):
#         print("inner func excuted")
#         print('x' * x)
#         print(*args,**kwargs)
#
#     print("outer func excuted")
#     print(inner.__closure__)
#     print(type(inner.__closure__))
#     print((str(inner.__closure__)))
#     return inner  # 调用执行inner()函数
#
#
# s = outer()  # 调用执行outer函数
#
#
#
#
#
# s('l',2,3,4,5,6,)

# from urllib.request import urlopen
#
# def index(url):
#     def get():
#         return urlopen(url).read()
#     return get
#
# python = index("http://www.baidu.com") # 返回的是get函数的地址
# print(python()) # 执行get函数《并且将返回的结果打印出
# print(type(python().decode()))
# print(python().decode())

def deco1(func):
    print('deco1 outer starting')

    def inner1(*args, **kwargs):
        print('deco1 inner starting')
        # func(*args, **kwargs)
        print('deco1 inner ending')
        return func(*args, **kwargs)

    print('deco1 outer ending')
    return inner1


def deco2(func):
    print('deco2 outer starting')

    def inner2(*args, **kwargs):
        print('deco2 inner starting')
        # func(*args, **kwargs)
        print('deco2 inner ending')
        return func(*args, **kwargs)

    print('deco2 outer ending')
    return inner2

def deco3(func):
    print('deco3 outer starting')

    def inner2(*args, **kwargs):
        print('deco3 inner starting')
        # func(*args, **kwargs)
        print('deco3 inner ending')
        return func(*args, **kwargs)

    print('deco3 outer ending')
    return inner2


# @deco1
# @deco2
# @deco3
def decorated(a, b):
    print('decorated function starting')
    print(f'{a} + {b} = {a + b}')
    print('decorated function ending')
    return a + b



# print(decorated(3, 8))#返回值是11
# decorated = deco1(decorated)#@所代表的意义
decorated(3, 8)
