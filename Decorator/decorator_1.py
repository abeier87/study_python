def dec(f):
    pass


@dec
def double(x):
    return x * 2

# 一定记住下面两行内容，这是装饰器的本质
# 5-7行代码完全等价于下面的代码
# double = dec(double)
