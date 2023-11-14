from ..sq import good
# from . import hello

def sayhi():
    print(__name__)
    good.saygood()
    print("Hi!")
    
if __name__=='__main__':
    print(__name__)
    hello.sayhello1()
    print('2+5~')