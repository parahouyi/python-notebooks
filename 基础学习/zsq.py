# class Foo(object):
#     def __init__(self):
#         pass
#
#     def __call__(self, func):
#         def _call(*args, **kw):
#             print('class decorator runing')
#             return func(*args, **kw)
#
#         return _call
#
#
# class Bar():
#     @Foo()
#     def bar(self, test, ids):   # bar = Foo()(bar)
#         print('bar')
#         print(test*2,ids*2)
#
# c = Bar()
# Bar().bar('aa', 'ids')
#
# c.bar('bb','hd')

# class Foo():
#     def __init__(self):
#         pass
#     def __call__(self,func):
#         def _call(*args,**kwargs):
#             print('class decorator is running')
#             return func(*args,**kwargs)
#
#         return _call
#
# class Bar():
#     @Foo()
#     def bar(self,test,ids):
#         print('bar')
#         print(test*2,ids*2)
#
#
# d = Bar()
# d.bar('hc','dd')

# def decoone(func):
#     def wrapper(*args,**kwargs):
#         print('deco one is starting')
#         result = func(*args,**kwargs)
#         print('deco one is ending')
#         return result
#     return wrapper
#
# def decotwo(func):
#     def wrapper(*args,**kwargs):
#         print('deco two is starting')
#         result = func(*args,**kwargs)
#         print('deco two is ending')
#         return result
#     return wrapper
#
# def decothree(func):
#     def wrapper(*args,**kwargs):
#         print('deco three is starting')
#         result = func(*args,**kwargs)
#         print('deco three is ending')
#         return result
#     return wrapper
#
# @decoone
# @decotwo
# @decothree
# def helop():
#     print('helop')
#
# helop()

class Decoclass():
    def __init__(self,func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print('this is the decoclass')
        res = self.func(*args,**kwargs)
        print('this is the end of decoclass')
        return res

@Decoclass
def func1(id):
    print(id*3)
    return 5

t = func1('sa')

print(t)