class Foo:
    def __init__(self):
        pass

    def __call__(self, func):
        def _call(*args, **kw):
            print('class decorator runing')
            return func(*args, **kw)

        return _call


class Bar:
    @Foo()
    def bar(self, test, ids):   # bar = Foo()(bar)
        print('bar')

Bar().bar('a','b')


@Foo()
def multiple(a,b):
    print(f'{a}*{b} = {a*b}')

multiple(3,9)

# class Foo2:
#     def __init__(self,func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         self.func(*args,**kwargs)
#         print('class decorator2 runing')
#
# @Foo2
# def add(a,b):
#     print(f'{a} + {b} = {a+b}')
# add(3,7)