'''
case 2:
当子类调用一个重名的函数时，Python 会按照 MRO 的顺序查找并调用第一个匹配的函数。
你可以通过 ClassName.__mro__ 属性查看类的 MRO。
'''

class A:
    def __init__(self):
        print("A's __init__")
        # super().say_hello()

    def say_hello(self):
        print("Hello from A")

class B:
    def __init__(self):
        print("B's __init__")
        # super().__init__(*args, **kwargs)
        
    def say_hello(self):
        print("Hello from B")

class C(A, B):
    def __init__(self, *args, **kwargs):
        print("C's __init__")
        super().__init__(*args, **kwargs)

# 创建 C 的实例
c = C()

c.say_hello()