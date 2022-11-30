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
# class Bar(object):
#     @Foo()
#     def bar(self, test, ids):   # bar = Foo()(bar)
#         print('bar')
# #
# #
# Bar().bar('aa', 'ids')

# class Foo():
#     def __init__(self, func):
#         self._func = func
#
#     def __call__(self):
#         print('class decorator runing')
#         self._func()
#         print('class decorator ending')
#
#
# @Foo
# def bar():
#     print('bar')
#
# bar()

class Classdeco:
    def __init__(self):
        print('class initialized')


    def __call__(self, func):
        print('the call method is starting')

        def inner(*args, **kwargs):
            print('the classdeocrator of call method is starting')
            return func(*args, **kwargs)

        return inner


@Classdeco
def add():
    print('the decorated fun is running the restult is')



# Classdeco().add(8,9)
