def dec(f):
    return 1


@dec
def double(x):
    return x * 2


# print(double(2))    # TypeError: 'int' object is not callable
print(double)   # 1
