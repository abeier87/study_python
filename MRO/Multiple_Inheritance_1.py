'''
case 1:
在这个例子中，C 的 __init__ 方法调用了 super().__init__()，这会根据 MRO 调用 A 的 __init__ 方法。
然后，A 的 __init__ 方法再次调用 super().__init__()，这会根据 MRO 调用 B 的 __init__ 方法。
因此，super() 的真正含义是根据 MRO 调用下一个类的方法，而不仅仅是直接父类的方法。
这使得多重继承中的方法调用更加灵活和强大。
'''

class A:
    def __init__(self, a):
        print("A's __init__")
        print(a)
        super().__init__(b=a)

class B:
    def __init__(self, b):
        print("B's __init__")
        print(b)

class C(A, B):
    def __init__(self, *args, **kwargs):
        print("C's __init__")
        super().__init__(*args, **kwargs)

# 创建 C 的实例
c = C(a=1)