
## git 命令

```

…or create a new repository on the command line

echo "# python_code" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:digmyth/python_code.git
git push -u origin master
…or push an existing repository from the command line

git remote add origin git@github.com:digmyth/python_code.git
git push -u origin master
```


## python模块导入知识
* __all__ 只用于from xx import * 形式导入起限定作用,记住有星

1 在定义一个模块时如md.py,写入了很多语句或变量,__all__可以限定别人from导入模块哪些变量或方法
 ```
 __all__ = ['x','func']
    x=1
    y=2
    def func():
        pass
```
2 在一个一个多级目录包下有很多模块时，别人from xx import * (只有from)导入可能找不到模块，这时可以在各个包的__init__.py文件里定义__all__指定包下哪些模块可以导入，有时问题得到解决.
问题： any.py里找不到c包
```
from app01.a.b import *

def func():
    return  c.c1.AdminSite()

x=func()
print(x)
```
解决：b包目录__init__.py定义__all__
```
__all__ = ['c',] # 在这种情况下__all__有着from app01.a.b import c 相同作用
```


3 只要导入（impor或from import）就会从上到下执行各个包的__init__.py文件，一般__init__.py文件定义该包下的模块导入. 
比如a包有b,c模块,那么a的__init__.py文件可以定义为from a import b,c

## 总结
在大多数情况下都需要在各个包__init__.py下定义from xx import xx来初始化包路径


```
def func():
    pass

x=func
import types
a=isinstance(x,types.FunctionType)
print(a)  # 判断一个字符串是不是函数
```

```
class Foo():
    def __init__(self,name,age):
        self.name = name
        self.age = age
obj = Foo("wxq",18)
x="name"

a=getattr(obj,x, "NotFound") # 通过字符串获取属性(反射)
print(a)
```

```
class A():
    def func1(self):
        return self.func2()

    def func2(self):
        print("A.func2")

class B(A):
    def func2(self):
        print("B.func2")

obj=B()
obj.func1()   # 这里打印"B.func2",也就是说先从调用对象找起
```
