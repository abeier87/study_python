<big>**module的概念**</big>

在Python中，module是组织单位，它自己独立构成一个命名空间。

实际应用中，module一般对应的是.py文件。当然这不是绝对的，也可以从其他类型的文件里面生成一个module。

需要注意的是，module是一个Python运行时的概念，它本身是一个Python object，在Python object里面，还可以有很多其他的Python object。module保存在内存里是Python级别的概念，而文件是操作系统级别的概念。**我们需要通过import，也就是“导入”这个过程从一个文件里生成一个module**。

**一个最简单的例子：**  
有两个.py文件，一个是[example.py](example.py)，另外一个是[test.py](test.py)
在example.py里面可以使用import test，把test.py里面写的内容变成一个module。

当执行import test的时候，  
1）把test作为名字来寻找这个module；  
2）检查缓存，是否有叫做test module已经被读取进来了；  
3）如果有的话，就不用下面这些load的过程，可以直接把它赋值给test；  
4）如果没有，就要寻找名字叫做test的module；  
5）在寻找的过程中，首先会检查这个名字是不是一个built in module（即，Python自带的module，如：sys, os, math等）；  
6）如果它不是built in module的话，就会在sys.path内寻找test.py文件，sys.path一般包括：这个文件所在的这个文件夹、Python自带的一些package（asyncio, multiprocessing）、还有site packages（即pip install的位置）。按顺序寻找，找到了就不再继续，因此要**注意命名冲突的问题**；  
7) 在寻找到符合条件的文件之后，它就会**在一个单独的命名空间里面运行这个文件**，也就是所谓的建立一个module。

比如在test.py里面，建立了一个class A，当我们import test时，就会新建一个module，然后在这个module里面定义一个class A，在完成这个module object时候，它会更新一下缓存，这样未来如果有其他的文件，其他的代码在import这个名字的时候，就不用再运行一次了，最后他会把这个module object赋值给这个叫做test的变量。也就是说在做完import test之后，test就可以作为一个变量被使用了。

为了让更好的理解，我们做一个实验，我们在test.py里面打印'test is imported'，同时在主文件example.py里面import test，可以看到这一行文字就被打印出来了，但即便我们尝试import若干次，它也只会打印一次。因为就像我们前面说的，它只会运行一遍这个代码，然后把这个module给缓存起来，在下一次import的时候，就会直接拿到这个缓存好的module。

<big>**package的概念**</big>

package就是一种特殊的module。

**区别package和module：**  
a. 在Python中package几乎和module有着一模一样的功能，它只是多了一个“ \_\_path\_\_ ”属性。

b. 在操作系统层级package往往对应的是一个文件夹。一个文件夹里面可以有其他的文件夹或者文件，但是一个文件里面不能有文件夹，所以一个package里面可以有其他的sub package，也可以有module，但是module在组织结构上就是最末端的一个东西。

c. import某个.py文件时，会执行这个文件，import某个文件夹时，会查看这个文件夹下有没有'\_\_init\_\_.py'文件，如果没有的话，就不会运行任何额外的代码；如果有的话，运行'\_\_init\_\_.py'。需要注意的是只会运行'\_\_init\_\_.py'，不会运行其他文件，当然Python也不知道其他文件的存在。如：[example_2.py](example_2.py)。

当我们import某个文件夹下的某个文件时，会先运行'\_\_init\_\_.py'（如果有的话），再运行这个文件。如：[example_3.py](example_3.py)。

d. 我们可以在'\_\_init\_\_.py'文件中使用'\_\_all\_\_ = []'，来选择暴露这个package中的某些module。如：[example_4.py](example_4.py)。

<big>**相对导入**</big>

相对导入会将相对路径转成绝对路径，需要满足以下两个条件：  
1. 导入代码所在的文件不能被作为主程序运行，由于主程序的'\_\_name\_\_'='\_\_main\_\_'，无法转成绝对路径，因此会导入失败。

2. 举一个具体的例子来说明：在' a.py '中导入' b.py '，导入语句中的文件夹级别要低于调用' a.py '的' .py '文件所在的文件夹。如：[example_6.py](example_6.py)可以运行，但是直接运行' package_3 '中的' hi2.py '的第3行就不行。

然而，常见用法举例2可以忽略上述两个条件。

<big>**常见用法举例**</big>

1. 导入同一个文件夹内的' .py '文件  
1.1 在' a.py '中导入' b.py '，' a.py '作为主程序，直接' import b '  
1.2 在' a.py '中导入' b.py '，' a.py '不是主程序，请看' package_2 '内的' \_\_init\_\_.py '

2. 导入不同文件夹内的' .py '文件  
在' package_3 '中的' hi3.py '中导入' package_1 '中的' hi.py '。

3. 连环导入（不知道是否常用，在别人的代码里遇到过）  
首先在' b.py '中导入' c.py '，如果我们想在' a.py '中导入' c.py '，除了直接导入，我们还可以from' b.py '导入' c.py '，如：[example_7.py](example_7.py)
