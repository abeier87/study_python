class grandpa:
    def __init__(self):
        print("a")
    
    def say_hello(self):
        print("hello from grandpa")


class f_1(grandpa):
    def __init__(self):
        print("f1")
        
    def say_hello(self):
        print("hello from f1")

class f_2(grandpa):
    def __init__(self):
        print("f2")
    
    def say_hello(self):
        print("hello from f2")
    

class son(f_1, f_2):
    def __init__(self):
        print("son")
        
son_1 = son()
son_1.say_hello()