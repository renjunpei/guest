from django.shortcuts import render
from django.http import HttpResponse,HttpResponsePermanentRedirect

def index(request):

    # return HttpResponse("Hello Django!")

    return render(request,"index.html")

# 登录
def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # 进行数据校验
        if not all([username, password]):
            # 数据不完整
            return render(request, 'index.html', {'error': '数据不完整'})
        if username == "admin" and password == "admin123":
            # return HttpResponse("login success")
            # return render(request,"event_mange.html")
            # return HttpResponsePermanentRedirect("/event_mange/")   # (HttpResponsePermanentRedirect)路径重定向，从而路径指向event_mange
            reponse = HttpResponsePermanentRedirect("/event_mange/")
            # reponse.set_cookie("user", username, 3600)    # 添加cookie
            request.session["user"] = username
            return reponse
        else:
            return render(request,"index.html",{"error":"用户名或密码错误"})

# 登录成功页面
def event_mange(request):
    # username = request.COOKIES.get("user","")
    username = request.session.get("user", "")

    return render(request,"event_mange.html",{'user': username})



# Create your views here.
