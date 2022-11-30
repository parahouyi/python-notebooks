
def digui(n):
    print(n,end = ' ')
    if n>0:
        digui(n-2)

digui(10)