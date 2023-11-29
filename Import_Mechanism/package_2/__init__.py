from package_2.better import saybetter
from package_2 import good

# 下面这种写法也可以
# from .better import saybetter
# from . import good

__all__ = ['saybetter', 'good']
