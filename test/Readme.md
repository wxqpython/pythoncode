
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
```
__all__ = ['md1', 'md2']
```


3 只要导入（impor或from import）就会从上到下执行各个包的__init__.py文件，一般__init__.py文件定义该包下的模块导入. 
比如a包有b,c模块,那么a的__init__.py文件可以定义为from a import b,c

