from django.shortcuts import render
from django.http import HttpResponse,HttpResponsePermanentRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def index(request):

    # return HttpResponse("Hello Django!")

    return render(request,"index.html")

# 登录
def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # 进行数据校验查看是否为空
        if not all([username, password]):
            # 数据不完整
            return render(request, 'index.html', {'error': '数据不完整'})
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session["user"] = username
            reponse = HttpResponsePermanentRedirect("/event_mange/")
            return reponse

        # # if username == "admin" and password == "admin123":
        #     # return HttpResponse("login success")
        #     # return render(request,"event_mange.html")
        #     # return HttpResponsePermanentRedirect("/event_mange/")   # (HttpResponsePermanentRedirect)路径重定向，从而路径指向event_mange
        #     reponse = HttpResponsePermanentRedirect("/event_mange/")
        #     # reponse.set_cookie("user", username, 3600)    # 添加cookie
        #     request.session["user"] = username
        #     return reponse
        else:
            return render(request,"index.html",{"error":"用户名或密码错误"})

# 登录成功页面
@login_required
def event_mange(request):
    # username = request.COOKIES.get("user","")
    username = request.session.get("user", "")

    return render(request,"event_mange.html",{'user': username})



# Create your views here.
