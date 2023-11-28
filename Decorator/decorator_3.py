import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print('Time elapsed: {}'.format(end - start))
        return ret
    return wrapper


@timer
def double(x):
    return x * 2


@timer
def add(x, y):
    return x + y


print(double(3))    # 6
print(add(2, 5))    # 7
