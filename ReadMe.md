当在数据库查到所有虚机的flavor属性，就可以计算资源占用比，便于资源可视化
```
import re
from functools import reduce

query_set = ["1C10G200G","2C10G200G","4C10G200G","8C10G200G","16C32G200G500G"]
class Cpu_Mem_Osdisk_Disk():
    def __init__(self,query_set):
        self.query_set = query_set

    def f1(self,x,y):
        return x+y

    def get_cpu_mem_osdisk_disk(self):
        vcpu_list = []
        memory_list = []
        osdisk_list = []
        disk_list = []
        for row in self.query_set:
            flavor = row
            ret = re.split("C|G",flavor)
            vcpu_list.append(int(ret[0]))
            memory_list.append(int(ret[1]))
            osdisk_list.append(int(ret[2]))
            disksize = ret[3]
            if len(disksize):
                disk_list.append(int(disksize))

        cpu_mem_osdisk_disk_dict = dict(
            used_vcpu = reduce(self.f1,vcpu_list,0),
            used_memory = reduce(self.f1,memory_list,0),
            used_osdisk =  reduce(self.f1,osdisk_list,0),
            used_disk = reduce(self.f1,disk_list,0)
        )
        return  cpu_mem_osdisk_disk_dict

if __name__ == '__main__':
    obj = Cpu_Mem_Osdisk_Disk(query_set)
    print(obj.get_cpu_mem_osdisk_disk())
    
```






































```
position
     position: relative  # 与absolute一起使用
     position: absolute  #随滚动条滚动而滚动
      随滚动条滚动而滚动，并且一直往上找，直到找到一个relative后进行定位
     position: fixed     # 永远在窗口某位置
```

