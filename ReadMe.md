
## 异步非阻塞

普通阻塞式socket 服务端
```
import socket
import time

sock = socket.socket()
sock.bind(('127.0.0.1',9999))
sock.listen(5)

def process_handler(client):
    data = client.recv(8096)
    print(data)
    client.sendall(b'/ HTTP/1.1  200 OK\r\n\r\ntest code ....')

while True:
    client,addr = sock.accept()
    process_handler(client)
    client.close()
```

非阻塞式socket服务端
```
import socket,select,time

sock = socket.socket()
sock.setblocking(False)
sock.bind(('127.0.0.1',9988))
sock.listen(10)

inputs = [sock,]

while True:
    r,w,e=select.select(inputs,[],[],0.05)

    for conn in r:
        if conn == sock:
            client,addr = sock.accept()
            client.setblocking(False)
            inputs.append(client)
        else:
            try:
                data=conn.recv(4096)
            except Exception as e:
                data = ""
            print(data)
            if data:
                conn.sendall(b'/ HTTP/1.1 200 OK\r\nHost: 127.0.0.1\r\n\r\nnwwwwx4')
            inputs.remove(conn)
            conn.close()
```

socket客户端批量并发请求(异步)验证socket服务端能否异步非阻塞式处理请求

socket_client01.py 多运行几个socket_client也可模拟
```
import socket

client = socket.socket()
client.connect(('127.0.0.1',8001))
while True:

    v = input(">>>")
    client.sendall(v.encode())
    ret = client.recv(1024)
    print("server response:",ret)
```

或者编写异步socket客户端
```
d
```







































```
position
     position: relative  # 与absolute一起使用
     position: absolute  #随滚动条滚动而滚动
      随滚动条滚动而滚动，并且一直往上找，直到找到一个relative后进行定位
     position: fixed     # 永远在窗口某位置
```

