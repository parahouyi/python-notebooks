import time, random


# def outer(func):  # 将index的地址传递给func
#     def inner():
#         start_time = time.time()
#         func()   # fun = index  即func保存了外部index函数的地址
#         end_time = time.time()
#         print("运行时间为%s"%(end_time - start_time))
#     return inner  # 返回inner的地址
#
#
# def index():
#     time.sleep(random.randrange(1, 5))
#     print("welcome to index page")
#
# index = outer(index)  # 这里返回的是inner的地址，并重新赋值给index
#
# index()

def timmer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res=func(*args,**kwargs) #res来接收home函数的返回值
        stop_time=time.time()
        print('run time is %s' %(stop_time-start_time))
        return res
    return wrapper

def home(name):
    time.sleep(random.randrange(1,3))
    print('welecome to %s HOME page' %name)
    return 123123123123123123123123123123123123123123
print(home('lucy'))

home = timmer(home)
print(home('simon'))