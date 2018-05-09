
from django.http import HttpResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
import requests
from .models import User,Ranking
# Create your views here.

def Get_openid(request):
    try:
        if request.method == 'GET':
            code = request.GET.get('code')
            r = requests.get(
                'https://api.weixin.qq.com/sns/jscode2session?appid=wx1526e3c09e45548d&secret=8361923982045d101ce1e17ebd6273a8&js_code=' + code + '&grant_type=authorization_code')
            code = json.loads(r.text)
            lis = (100, code)
            json_str = json.dumps(lis)
            return HttpResponse(json_str)
        else:
            lis3 = (103, 300)
            json_str = json.dumps(lis3)
            return HttpResponse(json_str)
    except:
        lis4 = (104, 300)
        json_str = json.dumps(lis4)
        return HttpResponse(json_str)

def Regist(request):
    print('Regist')
    try:
        if request.method == 'POST':
            _id_wx = request.POST.get('wxid')
            _photourl = request.POST.get('photourl')
            _name = request.POST.get('name')
            _user = User.objects.all().filter(id_wx=_id_wx)

            if _user :
                lis = (102,300)
                json_str = json.dumps(lis)
                return HttpResponse(json_str)
            else:
                user = User(id_wx=_id_wx,photourl = _photourl,name=_name)
                user.save()
                lis = (100, 300)
                json_str = json.dumps(lis)
                return HttpResponse(json_str)
        else:
            lis3 = (103, 300)
            json_str = json.dumps(lis3)
            return HttpResponse(json_str)
    except:
        lis4 = (104, 300)
        json_str = json.dumps(lis4)
        return HttpResponse(json_str)


#写入分数
def Write(request):
    print('Write')
    try:
        if request.method == 'POST':
            _id_wx = request.POST.get('wxid')
            _grade = request.POST.get('grade')
            _user = User.objects.get(id_wx = _id_wx)
            print(_grade)
            u = Ranking.objects.all().order_by('grade')
            print(u)

            print(u.last().grade)
            if u.__len__()>=100:
                if int(u.last().grade)>int(_grade):
                    myself = Ranking.objects.get(user=_user)
                    if myself:
                        print('myself')
                        myself.delete()
                    rank = Ranking(user = _user,name =_user.name,grade =_grade,photourl=_user.photourl)
                    rank.save()
            else:
                myself = Ranking.objects.filter(user=_user)
                if myself:
                    myself.delete()
                rank = Ranking(user=_user, name=_user.name, grade=_grade,photourl=_user.photourl)
                rank.save()

            Rank()
            lis = (100, 300)
            json_str = json.dumps(lis)
            return HttpResponse(json_str)
        else:
            lis3 = (103, 300)
            json_str = json.dumps(lis3)
            return HttpResponse(json_str)
    except:
        lis4 = (104, 300)
        json_str = json.dumps(lis4)
        return HttpResponse(json_str)

#sel为插入数据的本身角色，f即为其分数
def Rank():
    print("Rank")
    n=0
    rank = Ranking.objects.all().order_by('grade')
    print(rank)
    for i in rank:
        i.rangking = n+1
        i.save()
        n=n+1
        if n>100:
            i.delete()

def Q_rangking(request):
    print('Q_rangking')
    try:
        u = Ranking.objects.all().order_by('grade')
        paginator = Paginator(u, 5)  # Show 25 contacts per page
        # 以get的方法从url地址中获取页码
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
        data = serializers.serialize('json', contacts.object_list)
        lis = (100, data)
        json_str = json.dumps(lis)
        return HttpResponse(data)
    except:
        lis4 = (104, 300)
        json_str = json.dumps(lis4)
        return HttpResponse(json_str)