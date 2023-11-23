import time


def timeit(iteration):
    print('timeit called')

    def timer(func):
        print('timer called')

        def wrapper(*args, **kwargs):
            print('wrapper called')
            start = time.time()
            for _ in range(iteration):
                ret = func(*args, **kwargs)
            end = time.time()
            print('Time elapsed: {} after {} iterations'.format(
                (end - start), iteration))
            return ret

        return wrapper

    return timer


@timeit(100)
def double(x):
    return x * 2

# 等价于下面代码
# double = timeit(100)(double)


print(double(3))    # 6
