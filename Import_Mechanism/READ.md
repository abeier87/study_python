<big>**module的概念**</big>

在Python中，module是组织单位，它自己独立构成一个命名空间。

实际应用中，module一般对应的是.py文件。当然这也不是绝对的，我们可以从其他类型的文件里面生成一个module。  

需要注意的是，module是一个Python运行时的概念，它本身是一个Python object，在Python object里面，还可以有很多其他的Python object。module保存在内存里是Python级别的概念，而文件是操作系统级别的概念。**我们需要通过import，也就是“导入”这个过程从一个文件里生成一个module。**

<big>**package的概念**</big>

package就是一种特殊的module。

在Python中package几乎和module有着一模一样的功能，它只是多了一个“ \_\_path\_\_ ”属性。

之所以要区分package跟module，是因为在操作系统层级package往往对应的是一个文件夹。一个文件夹里面可以有其他的文件夹或者文件，但是一个文件里面不能有文件夹，所以一个package里面可以有其他的sub package，也可以有module，但是module在组织结构上就是最末端的一个东西。

a. 最简单的一个例子：  
有两个.py文件，一个是[example.py](example.py)，另外一个是[test.py](test.py)
在example.py里面可以使用import test，把test.py里面写的内容变成一个module。

当执行import test的时候，  
1）把test作为名字来寻找这个module；  
2）检查缓存，是否有叫做test module已经被读取进来了；  
3）如果有的话，就不用下面这些load的过程，可以直接把它赋值给test；  
4）如果没有，就要寻找这个名字叫做test module；  
5）在寻找的过程中，首先会检查这个名字是不是一个built in module（即，Python自带的module，如：sys, os, math等）；
6）如果它不是built in module的话，就会在sys.path内寻找test.py文件，sys.path一般包括：这个文件所在的这个文件夹、Python自带的一些package（asyncio, multiprocessing）、还有site packages（即pip install的位置）。按顺序寻找，找到了就不再继续，因此要注意命名冲突的问题；  
7) 在寻找到符合条件的文件之后，它就会**在一个单独的命名空间里面运行这个文件**，也就是所谓的建立一个module。

比如在test.py里面，建立了一个class A，当我们import test时，就会新建一个module，然后在这个module里面定义一个class A，在完成这个module object时候，它会更新一下缓存，这样未来如果有其他的文件，其他的代码在import这个名字的时候，就不用再运行一次了，最后他会把这个module object赋值给这个叫做test的变量。也就是说在做完import test之后，test就可以作为一个变量被使用了。

为了让更好的理解，我们做一个实验，我们在test.py里面打印'test is import'，同时在主文件example.py里面import test，可以看到这一行文字就被打印出来了，但即便我们尝试import若干次，它也只会打印一次。因为就像我们前面说的，它只会运行一遍这个代码，然后把这个module给缓存起来，在下一次import的时候，就会直接拿到这个缓存好的module。




总结：import某个.py文件时，会执行这个文件，import某个文件夹时，会执行'\_\_init\_\_.py'文件。  
相对导入会将相对路径转成绝对路径，导入与主程序所在的同一个文件夹下其他.py文件时，由于'\_\_name\_\_'='\_\_main\_\_'，无法转成绝对路径，因此会导入失败。

" \_\_all\_\_ = [] " 的用法

