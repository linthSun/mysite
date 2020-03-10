from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User  # 导入django自带的user表



def index(request):
    return render(request, 'index.html')

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        result = auth.authenticate(username=username, password=password)  # 用户认证
        if result is not None:  # 如果数据库里有记录
            auth.login(request, result)  # 登陆成功
            return render(request, 'index.html')
        else:  # 数据库里不存在与之对应的数据
            return render(request, 'login.html', {'login_error': '用户名或密码错误'})  # 注册失败
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'index.html')





