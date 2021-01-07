from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# request--environ 请求相关数据，为HTTPRequest对象
def home(request):
    # render方法用来打开html文件，对文件进行模板渲染
    # 参数一：request
    # 参数二：html文件路径（在templates文件夹下面的Html页面会被自动识别到）
    # 渲染完成后，返回响应页面数据并传递给wsgi文件中的socket，最终页面数据返回给客户端
    return render(request, 'home.html')


def hello(request):
    # context是一个字典，里面存储传递的变量
    return render(request, 'hello.html', context={"title": "这是一个例子", "name": "打工人"})


def article_detail(request, article_id):
    return HttpResponse('文章id：%s' % article_id)