
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
有关多级数据处理
```
# same QuerySet type
comment_list=[
    {'nid':1,'content':111,'parent_id':None},
    {'nid':2,'content':222,'parent_id':None},
    {'nid':3,'content':333,'parent_id':None},
    {'nid':4,'content':444,'parent_id':1},
    {'nid':5,'content':555,'parent_id':4},
    {'nid':6,'content':666,'parent_id':1},
    {'nid':7,'content':777,'parent_id':2},
]

for i in comment_list:
    i['children']=[]
d={}
for i in comment_list:
    d[i['nid']]=i
ret=[]

# for k,v in d.items():
#     print(k,v)

for k,v in d.items():
    if v["parent_id"]:
        x=v["parent_id"]
        d[x]['children'].append(v)

    else:
        ret.append(v)

for  i in ret:
    print(i)
```
形如QuerySet的数据类型转为了嵌套型数据类型
```
{'nid': 1, 'content': 111, 'parent_id': None, 'children': [{'nid': 4, 'content': 444, 'parent_id': 1, 'children': [{'nid': 5, 'content': 555, 'parent_id': 4, 'children': []}]}, {'nid': 6, 'content': 666, 'parent_id': 1, 'children': []}]}
{'nid': 2, 'content': 222, 'parent_id': None, 'children': [{'nid': 7, 'content': 777, 'parent_id': 2, 'children': []}]}
{'nid': 3, 'content': 333, 'parent_id': None, 'children': []}
```

