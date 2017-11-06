from django.shortcuts import render,HttpResponse,redirect
from web.models import *
from web.form import *
# Create your views here.


def Signup(reuqest):
    if reuqest.method == 'POST':
        # user = reuqest.POST.get("username")
        # u = UserInfo.objects.filter(username=user)  #在数据库中查询用户名是否重复
        # erro = ""
        # if u :
        #     erro = "该用户名已存在！"
        #     return render(reuqest,"signup.html",{"erro":erro})
        # elif user == "":
        #     erro ="用户名不能为空！"
        #     return render(reuqest, "signup.html", {"erro": erro})
        # else:
        #     pwd = reuqest.POST.get("password")
        #     confirm_pwd = reuqest.POST.get("confirm_password")
        #     erro1 = ""
        #     if pwd != confirm_pwd:
        #         erro1 = "密码输入不一致！"
        #         return render(reuqest, "signup.html", {"erro1": erro1})
        #     elif pwd == "":
        #         erro1 = "密码不能为空！"
        #         return render(reuqest, "signup.html", {"erro1": erro1})
        #     else:
        #         erro2=""
        #         email = reuqest.POST.get("email")
        #         if email =="":
        #             erro2 = "邮箱不能为空！"
        #             return render(reuqest, "signup.html", {"erro1": erro2})
        #         else:
        #             UserInfo.objects.create(username=user,password=pwd,email=email)
        #             return redirect("/web/home/")
        obj = Sign_up(reuqest.POST)
        if obj.is_valid():
            UserInfo.objects.create(**obj.cleaned_data)
            return redirect("/web/home/")
        else:
            return render(reuqest, "signup.html", {'obj': obj})
    if reuqest.method == 'GET':
        return render(reuqest,"signup.html")
def Index(reuqest):
    if reuqest.session.get('is_login',None):     #验证是否登陆，如果登陆无需再次登陆
        articlelist = Article.objects.all()
        categorylist = Category.objects.all()
        return render(reuqest,"index.html",{"articlelist":articlelist,
                                            "categorylist":categorylist,
                                            "user":reuqest.session['user']})
    else:

        articlelist = Article.objects.all()
        categorylist = Category.objects.all()
        return render(reuqest, "index.html", {"articlelist": articlelist,
                                              "categorylist": categorylist,
                                              "user":None})


def base(reuqest):
    return render(reuqest,"base.html")
def Login(reuqest):
    if reuqest.method == "GET":
        if reuqest.session.get('is_login',None):  #验证是否登陆，如果登陆无需再次登陆
            return redirect("/web/index/")
        else:
            return render(reuqest,"login.html")
    if reuqest.method == "POST":
        user = reuqest.POST.get("username")
        pwd = reuqest.POST.get("password")
        obj = UserInfo.objects.filter(username=user,password=pwd)
        if obj:
           reuqest.session['user']=user
           reuqest.session['is_login'] =True
           return redirect('/web/index/')
        else:
            erro="用户名或密码错误！"
            return render(reuqest,"login.html",{"erro":erro})

def Home(request):
    if request.session.get('is_login',None):    #验证是否登陆，如果登陆无需再次登陆
        user_id =UserInfo.objects.filter(username=request.session['user']).values("id")
        articlelist = Article.objects.filter(author_id = user_id).values('title','content','category__caption','create_time','author__username','article_type__caption')
        return render(request,"home.html",{"user":request.session['user'],
                                           "articlelist":articlelist,})

    else:
        return redirect("/web/index/")
def Admin(reuqest):
    if reuqest.method == "GET":
        if reuqest.session.get('is_login',None): # 验证是否登陆，如果登陆无需再次登陆
            user_id = UserInfo.objects.filter(username=reuqest.session['user']).values("id")
            articlelist = Article.objects.filter(author_id=user_id).values('title', 'content')
            return render(reuqest,"admin.html",{"user":reuqest.session['user'],
                                                "articlelist":articlelist})
        else:
            return redirect("/web/index/")
    if reuqest.method =="POST":
        title = reuqest.POST.get("title")
        content = reuqest.POST.get("content")
        user_id = UserInfo.objects.filter(username=reuqest.session['user']).values("id")
        Article.objects.filter(author_id=user_id).update(title=title,content=content)
        return render(reuqest,"admin.html")
def Logout(reuqest):
    reuqest.session.clear()
    return redirect('/web/index/')

def Xiangxi(reuqest):
    if reuqest.method == "GET":
        if reuqest.session.get('is_login',None): # 验证是否登陆，如果登陆无需再次登陆
            categorylist=Category.objects.all()
            id = reuqest.GET.get("nid")
            print(id)
            article_list = Article.objects.filter(category_id=id)
            return render(reuqest,"xiangxi.html",{"user":reuqest.session['user'],
                                                  "categorylist":categorylist,
                                                "article_list":article_list})
        else:
            categorylist = Category.objects.all()
            id = reuqest.GET.get("nid")
            print(id)
            article_list = Article.objects.filter(category_id=id)
            return render(reuqest, "xiangxi.html", {"user": None,
                                                    "categorylist": categorylist,
                                                    "article_list": article_list})

