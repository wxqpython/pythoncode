
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


己知对象找所有封装属性，self.__class__.__dict__
己知对象找类名，self.__class__.__name__ 或 type(self)

有用代码片段
```
class A():
    pass
class C1(A):
    pass
class C2(A):
    pass

class Foo():
    a = C1()
    b = C2()

obj = Foo()
obj.a = 'xx'
dic = {}
for name,field in obj.__class__.__dict__.items():
    if isinstance(field,A):
        setattr(obj,name,field)
        dic[name] = field
print(obj.a)
print(dic)
```

对象动态添加属性
```
class A():
    def __init__(self):
        setattr(self, 'name','wxq')

class Foo(A):
    a = 1
    b = 2

obj = Foo()
print(obj.name)
```

