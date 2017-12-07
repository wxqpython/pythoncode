from django.shortcuts import render,HttpResponse,redirect

from app01 import models

def ck(request):
    print(request.COOKIES)
    obj = render(request, "ck.html")
    # models.UserInfo.objects.create(username="user1",pwd=123)
    # models.UserInfo.objects.create(username="user2",pwd=456)
    # obj.set_cookie('nnn', 123123)   # cookies写到浏览器上的键值对

    return obj

def login(request):
    if request.method == "GET":
        return render(request,"login.html")

    else:

        u=request.POST.get("user")
        p=request.POST.get("pwd")
        ct=models.UserInfo.objects.filter(username=u, pwd=p).count()
        if ct:
            obj =  redirect("/home/")
            #1  cookies的用法示例
            # obj.set_cookie("uuu", u, max_age=10)
            # 2 session的用法示例
            '''
            1 生成随机字符串发送给客户端
            2 保存在服务端
            3 并在服务端写session字典： 如用户名或密码
            '''
            request.session['user'] = u  # 写入的用户名
            request.session['pwd'] = p   # 写入的密码

            return  obj
        else:
            return render(request, "login.html",{"msg":"用户名或密码错误"})

def home(request):

    # v=request.COOKIES.get('uuu')
    v=request.session.get('user')  #   #对写入的用户名读出来
    if v:
        return  HttpResponse("welcome to home")
    else:
        return redirect("/login")

