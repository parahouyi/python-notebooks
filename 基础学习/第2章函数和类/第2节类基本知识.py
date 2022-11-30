from main import printer


# class Foo:
#     def __init__(self):
#         self.name = 'xxx'
#         self._age = 18
#         self.__sex = 'female'
#
#
# simon = Foo()
# printer(simon.name)
# printer(simon._age)
# printer(simon._Foo__sex) #私有变量被修饰，前面加上一个下划线再加上类名才能访问
# printer(dir(simon))
class People:
    '''new 是类方法，init是实例方法
    为什么有了new创建实例时只执行new方法，不能执行init方法呢'''
    # def __new__(cls, *args, **kwargs):
    #     print('{} is working to make a new one'.format(cls))
    def __init__(self, name = None):
        print('this is the init function')
        self.name = name
    def speak(self):
        print('i am a person')

class American(People):
    def __init__(self,name = None):
        super().__init__()
    def speak(self):
        print('i am a american')

p2 = People('simon')
p1 = American()
p2.speak()
