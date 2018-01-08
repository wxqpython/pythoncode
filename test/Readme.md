
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


## from import导入知识

1 在定义一个模块时如md.py,写入了很多语句或变量,__all__可以限定别人导入模块哪些变量或方法
 ```
 __all__ = ['x','func']
    x=1
    y=2
    def func():
        pass
```
2 在一个包下有很多模块，别人导入时找不到模块时，可以在该包的__init__.py文件里定义__all__指定包下哪些模块可以导入
```
__all__ = ['md1', 'md2']
```

3 只要导入就会从上到下执行各个包的__init__.py文件
一般__init__.py文件定义该包下的模块导入。比如a包有b,c模块
那么a的__init__.py文件定义为from a imprt b,c

