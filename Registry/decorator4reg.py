'''
Case1:
__setitem__(self, key, value)允许我们使用[]操作符向对象中添加键值对，如：add函数中的self[key] = value
'''

class Register:
    def __init__(self, name):
        self._dict = {}
        self._name = name
    
    def __setitem__(self, key, value):
        self._dict[key] = value
    
    def __getitem__(self, key):
        return self._dict[key]
    
    def register(self, target):
        
        def add(key, value):
            self[key] = value
            return value

        return lambda x: add(target, x)


'''
Case2:
我们也可以不使用__setitem__方法，而是使用一个普通的方法来实现相同的功能，如下：
'''

class Register2:
    def __init__(self, name):
        self._dict = {}
        self._name = name
    
    def __sample__(self, key, value):
        self._dict[key] = value
    
    def __getitem__(self, key):
        return self._dict[key]
    
    def register(self, target):
        
        def add(key, value):
            self.__sample__(key, value)
            return value
        return lambda x: add(target, x)


register = Register2('add+sub')

@register.register('add')
def ADD():
    print("a + b")

@register.register('sub')
def SUB():
    print("a - b")

register['add']()
register['sub']()