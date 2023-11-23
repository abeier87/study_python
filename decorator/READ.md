<big>**要理解装饰器首先要理解闭包的概念**</big>

    1. Closure (闭包)
**闭包 = 环境 + 控制**

广义的闭包：闭包函数\
狭义的闭包：函数访问外层作用域的变量这种现象

闭包之所以不会被销毁是因为，内部函数被return出去赋值给了全局变量，GC (Garbage Collection)不会回收windows下可以访问的变量，而子函数有保存父函数的作用域，指向父函数，因为子函数不会被销毁，所以父函数也不会被销毁。

闭包举例：[closure_func.py](closure_func.py)

    2. Decorateor (装饰器)
装饰器允许我们包装另一个函数，以扩展包装函数的行为，而无需修改基础函数定义。
一般来说，装饰器输入是一个函数，返回值也是一个函数。

a. 简单例子：[decorator_1.py](decorator_1.py)

b. 输入是函数，输出也可能不是函数：[decorator_2.py](decorator_2.py)

c. 给多个函数增加一个运行计时功能：[decorator_3.py](decorator_3.py)

d. 带参数的装饰器：[decorator_4.py](decorator_4.py)