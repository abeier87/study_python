# 我想要导入package_1中的hi.py3
import sys
sys.path.append('..')    # 将当前目录的上一级目录添加到sys.path中
from package_1 import hi

# hi.sayhi()


def sayhi2():
    hi.sayhi()
