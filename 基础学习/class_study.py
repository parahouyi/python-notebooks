import pywin.mfc.afxres


# class Person:
#
#     __age = 20
#
#     @property
#     def age(self):
#         print('read the age property')
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         print('setting the age property')
#         self.__age = value
#
#     @age.deleter
#     def age(self):
#         del self.__age

class Person:

    __age = 20


    def get_age(self):
        print('read the age property')
        return self.__age


    def set_age(self, value):
        print('setting the age property')
        self.__age = value


    def del_age(self):
        del self.__age

    age = property(get_age, set_age, del_age, 'come on property')


p = Person()
print(type(p.age))
print(Person.age)
print(Person().age)
print(p.__dict__)