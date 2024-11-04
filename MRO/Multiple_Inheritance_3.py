'''
case 3:
多次继承
'''

class A:
    def __init__(self):
        pass
        # print("SQ's __init__")

    def say_hello(self):
        print("Hello from SQ")


class B(A):
    def __init__(self, b):
        self.b = b

    def plus(self):
        print(self.b+1)

class C(B):
    def __init__(self, c):
        self.c = c
        super().__init__(c)
        
    def square(self):
        print(self.c**2)

# 创建 C 的实例
c = C(c=3)
c.plus()
c.square()