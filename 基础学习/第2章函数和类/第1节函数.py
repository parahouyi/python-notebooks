def printing(a,b,c,d=None,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(d)
    print(*args)
    print(**kwargs)

printing('a','b','c','ddd',1,2,3,4,5)
printing(b='ss',a='tt',c='ddde',d='edgd',)

def printinfo(a):
    print(a)
    print(f'此对象的类型是：{type(a)}')
    print(f'此对象的地址是：{id(a)}')
    try:
        print(f'此对象的长度是：{len(a)}')
    except:
        print('no lenth of this type')
ls=['2','tg','iu']
printinfo(ls)
n = 8768
printinfo(n)