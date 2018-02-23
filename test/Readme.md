
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




## 其它
类对象调用方法时永选先从自己类查找，然后才是查找父类，这一点很重要
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
