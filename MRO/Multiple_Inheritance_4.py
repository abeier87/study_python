class a:
    def __init__(self):
        print("a")

class b(a):
    def __init__(self):
        print("b")
        
sq = b()