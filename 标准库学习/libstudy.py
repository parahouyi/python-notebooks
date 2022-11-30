
def libstudy(a):
    print(exec(a).__name__)
    print(exec(a).__dict__)
    print(help(exec(a)))
    print(dir(exec(a)))