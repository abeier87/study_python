from sq.good import saygood
# from . import hello

saygood()


def sayhi():
    print(__name__)
    saygood()
    print("Hi!")

# if __name__=='__main__':
#     print(__name__)
#     hello.sayhello1()
#     print('2+5~')
