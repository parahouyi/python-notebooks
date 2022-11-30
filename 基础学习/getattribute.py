class A():
    a = 5
    def __init__(self, x):
        self.x = x

    def hello(self):
        return 'hello func'

a = A(10)

print(getattr(a, 'x'))  #相当于a.x
print(getattr(a, 'y', 20))  #相当于a.y，因为a.y并不存在，所以返回第三个参数作为默认值
print(getattr(a, 'hello'))  # 相当于a.hello()

print(getattr(A, 'a'))