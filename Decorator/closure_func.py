# 闭包，起到了变量封装的效果

def foo():
    v = 1

    def add():
        nonlocal v
        v += 1

    def get():
        return v

    return add, get


add1, get1 = foo()
add2, get2 = foo()
add1()
print(get1())    # 2
print(get2())    # 1
add1()
add1()
add1()
print(get1())    # 5
print(get2())    # 1
