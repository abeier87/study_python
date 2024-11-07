class grandpa:
    def __init__(self):
        print("a")
    
    def say_hello(self):
        self.real_say_hello()
        
    def real_say_hello(self):
        raise NotImplementedError("Subclass must implement abstract method")


class f_0(grandpa):
    def __init__(self):
        print("f0")

    # def real_say_hello(self):
    #     print("hello from f_0")


class f_1(f_0):
    def __init__(self):
        print("f1")
    
    def real_say_hello(self):
        super().real_say_hello()
        print("hello from f_1")


class f_2(grandpa):
    def __init__(self):
        print("f2")

    def real_say_hello(self):
        print("hello from f_2")

class son(f_1, f_2):
    def __init__(self):
        print("son")
    
    def real_say_hello(self):
        print("hello from son")

        
son_1 = son()
son_1.say_hello()
print(son_1.__class__.mro())