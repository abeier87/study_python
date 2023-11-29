import package_2 as p2

print(dir(p2))

p2.good.saygood()
p2.saybetter()
p2.saygooood()    # 报错，因为在__init__.py的__all__中没有暴露saygooood()函数
