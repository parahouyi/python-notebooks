def printer(a):
    print(f'变量的值是：{a}')
    print(f'变量类型是：{type(a)}')
    print(f'变量地址是：{id(a)}')
    try:
        print(f'变量长度是：{len(a)}')
    except:
        print('此类型没有长度')


# name = 'simon'
#
# # printer(str(map(list,name)))
# #
# # printer('comeone')
#
# a = 'simon'
# b = 'world'
# c = ((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))
# d = {6, 7, 8, 9, 10}
# e = {'Aa', 'Bb', 'Cc', 'Dd', 'Ee'}
# f = {'name': 'lucy', 'age': 18, 'sex': 'female', 'height': 170, 'weight': 34}
#
# zipf = zip(a, b, c, d, e, f)
#
# # printer(set(zipf))
#
# l1 = [2, 3, 3, 4, 3, 2, 3]
# l1.count(2)


# # def get_middle(s):
# #     return s[len(s) // 2] if len(s) % 2 else s[len(s) //2 - 1: len(s) // 2+1]
# def get_middle(s):
#     return s[(len(s) - 1) // 2:len(s) // 2 + 1]
#
#
# print(get_middle('testing2'))


# def find_uniq(arr):
#     sett = set(arr)
#     for i in arr[0:3]:
#         if arr[0:3].count(i) >= 2:
#             sett.remove(i)
#             break
#     n = sett.pop()
#     return n
#
#
# #
# print(find_uniq([3, 3, 3, 3, 3, 2]))

#
# a,b,c = map(int,input().split())
# print((a+b)*c)
# a = input()
# b = input()
# print(b[:2]+a[2:],a[:2]+b[2:],sep = '\n')

# a,b = input().split()
# print(a[:2]+b[:2])
# f = open('answer.doc','w')
# f.write(a[:2]+b[:2])
# f.close()
