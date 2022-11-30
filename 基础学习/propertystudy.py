from mytest.printing import printing


class Student:
    '''
    自定义一个学生类，来管理班级里所有的学生的基本信息
    '''

    def __init__(self):
        self._age = None
    #
    # def get_age(self):
    #     print('获取属性时执行的代码')
    #     return self._age
    #
    # def set_age(self, age):
    #     print('设置属性时执行的代码')
    #     self._age = age
    #
    # def del_age(self):
    #     print('删除属性时执行的代码')
    #     del self._age
    #
    # age = property(get_age, set_age, del_age, '学生年龄')


class Student:
    def __init__(self):
        self._age = None


    @property
    def age(self):
        print('获取属性时执行的代码')
        return self._age

    @age.setter
    def age(self, age):
        print('设置属性时执行的代码')
        self._age = age

    @age.deleter
    def age(self):
        print('删除属性时执行的代码')
        del self._age


stu = Student()
print(stu.__dict__)
# print(stu.__doc__)
stu.age = 29
print(stu.__dict__)

setattr(stu,'age',33)
print(stu.__dict__)

print(vars(stu))
