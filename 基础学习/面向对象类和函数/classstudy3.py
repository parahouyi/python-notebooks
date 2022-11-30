# class A:
#
#     def __init__(self):
#         print('i am class A')
#
#     def foo(self):
#         print('i am another class A')
#
#
# class B(A):
#
#     def __init__(self):
#         super().__init__()
#         print('i am class B')
#
#     def foo(self):
#         print('i am another class B')
#
#
# class C(B):
#
#     def __init__(self):
#         A.__init__(self)
#         print('i am class C')
#
#     def foo(self):
#         print('i am another class C')
#
#
# c = C()
import sys


class Study:

    def __init__(self, name='FengMei'):
        self.name = name

    def __del__(self):
        print('del')

    def getName(self):
        print(self.name)

    def __repr__(self):
        return "Study('xiaodeng')"


if __name__ == '__main__':
    car = Study()
    print(car)
    print(type(car))
    b = repr(car)
    print(b)
    print(type(b))
    c = eval(b)
    print(c)
    print(type(c))
