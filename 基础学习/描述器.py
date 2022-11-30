
class Age:
    def __get__(self, instance, owner):
        print('get:', self, instance, owner)
    def __set__(self, instance, value):
        print('set:', self, instance, value)
    def __del__(self):
        print('del')

class Person:
    def __getattribute__(self, item):
    age = Age()

p = Person()
# p.age = 20
p.age
# print(Person.age)
