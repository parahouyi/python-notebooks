class Person:
    '''
this is the first class defined by myself
'''

    species = 'human'
    born_order = 0

    def __init__(self, height, sex):
        self.height = height
        self.sex = sex

        def printinfo():
            print('create a person who is a {} and {} centimeters high'.format(self.sex, self.height))

        printinfo()

        Person.born_order += 1
        print(f'this person is the number {Person.born_order} person created')

    def __call__(self, func):
        print('this is the call method running')

        def _call(*args, **kwargs):
            func(*args, **kwargs)

        return _call

    def __del__(self):
        print(f'{self.__class__} is deleted')

    def speak(self, name):
        print('my name is {}'.format(name))
        self.name = name

    def walk(self, distance):
        print('move {} meters'.format(distance))


simon = Person(170, 'male')

print(simon.species)
print(Person.species)
simon.speak('simon')
print(simon.name)
simon.walk(5)
lucy = Person(163, 'female')

print(type(lucy))

# @Person()
# def decorated2():
#     print('this is the 2nd decorated method')
#
#
# @Person()
# def add(a, b):
#     print(f'{a}+{b} = {a + b}')
#     return a + b
#
#
# add(3, 9)
#
#
# class Operation:
#
#     @Person()
#     def multiple(self,a, b):
#         print(f'{a}*{b} = {a * b}')
#
#
# c = Operation()
#
# c.multiple(8,9)
#
# print(c)

print(Person.__doc__)
print(Person.__bases__)
print(Person.__flags__)

print(Person.__module__)
print(Person.__dict__)


# print(Person.__born_order)

class Sportsman(Person):

    def __init__(self, height, sex, major):
        super().__init__(height, sex)
        self.height = height
        self.sex = sex
        self.major = major
        def printinfo():
            print('a sportsman is created who is {} and a {} and also major in {}'.format(height, sex, major))
        printinfo()


lining = Sportsman(180, 'male', 'gymnastic')

lining.speak('lining')

liuxuan = Sportsman(170,'female','jumpingwater')

print(Person.born_order)

print(isinstance(liuxuan, Person))
del liuxuan
print(isinstance(simon, Sportsman))