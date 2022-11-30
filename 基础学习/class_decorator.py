
class check:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print('call')
        self.func()
@check
def fashuoshuo():
    print('发说说')

fashuoshuo()

class Person:
    pass
class People:
    pass

p1 = Person()
p2 = p1
print(p2)
# p1 = People()
print(p2)

import sys

print(sys.getrefcount(p2))
