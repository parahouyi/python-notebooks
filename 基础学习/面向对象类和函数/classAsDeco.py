class Deco:

    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('this is the call method of class Deco')
        return self.func(*args,**kwargs)

class Greeting:

    @Deco
    def hello(a):

        print('hello world')
        print(a)

    def hello2(self,a):

        print('hello world')
        print(a)

Greeting().hello('my')

# Greeting.hello2('hi')

c = Greeting()
c.hello('sss')

c.hello2('sss2')

