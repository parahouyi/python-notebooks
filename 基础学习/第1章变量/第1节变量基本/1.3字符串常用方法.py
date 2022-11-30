a = 'Life CAN BE GoOD LifE cAN be Bad LiFe IS MOSTly chEeRfUL buT sOMETIMES SAD'
b = a.replace(' ', '')
flag = ''
for i in b:
    if i.isupper() == True:
        flag += 'A'
    else:
        flag += 'B'

print(flag)
print(flag.translate(''.maketrans('AB', 'BA')))

print(flag.center(100, '*'))

print(flag[0: -1])
print(flag[0:-1] == flag[:-1])
