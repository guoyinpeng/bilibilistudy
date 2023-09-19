from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.models import Department,UserInfo

# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")


def user_list(request):
    return render(
        request,
        "user_list.html"
    ) # user_list.html为模板文件名


def user_add(request):
    return render(
        request,
        "user_add.html"
    )  # user_list.html为模板文件名


def tpl(request):
    name = "河科大最牛人才"
    roles = ["张宇", "郭寅鹏", "没有了"]
    user_info = {"name": "张宇", "salary": 5000000, 'role': "股东"}

    data_list = [
        {"name": "郭寅鹏", "salary": 10000, 'role': "总裁"},
        {"name": "姜智中", "salary": 10, 'role': "保安"},
        {"name": "其他人员", "salary": 1, 'role': "撑场面"},
    ]
    return render(
        request,
        'tpl.html',
        {
            "n1": name,
            "n2": roles,
            "n3": user_info,
            "n4": data_list
        }
    )


def something(request):
    # request是一个对象，封装了用户发送过来的所有请求相关数据

    # 1.获取请求方式 GET/POST
    print(request.method)

    # 2.在URL上传递值 /something/?n1=123&n2=999
    print(request.GET)

    # 3.在请求体中提交数据
    print(request.POST)

    # 4.【响应】HttpResponse("返回内容")，字符串内容返回给请求者。
    # return HttpResponse("返回内容")

    # 5.【响应】读取HTML的内容 + 渲染（替换） -> 字符串，返回给用户浏览器。
    return render(request, 'something.html', {"title": "来了"})

    # 6.【响应】让浏览器重定向到其他的页面
    # return redirect("https://www.baidu.com")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    # 如果是POST请求，获取用户提交的数据
    # print(request.POST)
    username = request.POST.get("user")
    password = request.POST.get("pwd")
    if username == 'root' and password == "123":
        # return HttpResponse("登录成功")
        return redirect("http://www.chinaunicom.com.cn/")

    # return HttpResponse("登录失败")
    return render(request, 'login.html', {"error_msg": "用户名或密码错误"})





#筛选性的获取数据
def orm(request):
    models.UserInfo.objects.all().update(password=888)
    models.UserInfo.objects.filter(id=4).update(age=999)
    models.UserInfo.objects.filter(name="郭寅鹏").update(age=18)
    return HttpResponse("更新数据成功")


def info_list(request):
    # 1.获取数据库中所有的用户信息
    # [对象,对象,对象]
    data_list = UserInfo.objects.all()

    # 2.渲染，返回给用户
    return render(request, "info_list.html", {"data_list": data_list})


def info_add(request):
    if request.method == "GET":
        return render(request, 'info_add.html')

    # 获取用户提交的数据
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")

    # 添加到数据库
    UserInfo.objects.create(name=user, password=pwd, age=age)

    # 自动跳转
    # return redirect("http://127.0.0.1:8000/info/list/")
    return redirect("/info/list/")


def info_delete(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/info/list/")

