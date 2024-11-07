class grandpa:
    def __init__(self):
        print("a")
    
    def say_hello(self):
        print("hello from grandpa")


class f_1(grandpa):
    def __init__(self):
        print("f1")


class f_2(grandpa):
    def __init__(self):
        print("f2")

    

class son(f_1, f_2):
    def __init__(self):
        print("son")
        self.say_hello()
        
son_1 = son()