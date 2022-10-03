import datetime
from email.mime import image
import time
import threading
import sqlite3
from random import randint, random
from typing import Counter
from urllib import response
from django.forms import modelform_factory
from django.shortcuts import redirect, render
from django.http import HttpResponse
import datetime as d
import  json
import urllib.request 
import ssl
from django.contrib import messages
from app.models import Profile, Server_Page,Status,Post
from django.contrib.auth import authenticate, login, logout
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
minecraft_dict = {}

def info_from_server(minecraft_server):
    """
    func are get a url dic and return info on the server
    """
    off_or_on=minecraft_server["online"]
    ip=minecraft_server["ip"]
    if off_or_on == True:
        player=int(minecraft_server["players"]["online"])
        version_minecraft=minecraft_server["version"]
        info={"online":off_or_on,"ip":ip,"player":player,"version":version_minecraft}
    else:
        info={"online":off_or_on,"ip":ip,"player":"0","version":"Server Close"}
    return info

def update_url(url):
    context = ssl._create_unverified_context()
    r = urllib.request.urlopen(url, context=context)
    results= r.read().decode()
    minecraft_results=json.loads(results)
    return minecraft_results

def player_time():
    while True:
        time.sleep(10)
        minecraft_dict
        date=datetime.datetime.now()
        rightnow=date.strftime("%x %X")
        for k,v in minecraft_dict.items():
            print("key : !!!",k)
            print("value : !!!",v)
            user_model = User.objects.get(username=k)
            new_time=Status.objects.create(user=user_model,time=rightnow,players=v["player"],name=k)
            new_time.save()
        time.sleep(15*60)

def minecraft_dict_update():
    global minecraft_dict 
    while True:
        connect_SQL=sqlite3.connect('MineBook\\db.sqlite3')
        c =connect_SQL.cursor()
        c.execute("SELECT ip,server_name FROM app_server_page")
        ip_and_name= c.fetchall()
        # time_and_player= c.fetchall()
        # b=0
        # for i in time_and_player:
        #     i=str(i[0])+str(i[1])
        #     if b==i:
        for ip in ip_and_name:
            url="https://api.mcsrvstat.us/2/"+str(ip[0])
            if url == "https://api.mcsrvstat.us/2/":
                continue
            print(ip)
            server_dict=info_from_server(update_url(url))
            server_dict["ip"]=ip[0]
            if server_dict["online"] == True:
                server_dict["online"]= "On"
                if len(server_dict["version"]) > 14:
                    server_dict["version"] = server_dict["version"][0:5]+"-1.19x"
            else:
                server_dict["online"]="Of"
            ip=ip[1]
            minecraft_dict.update({ip:server_dict})
            new = sorted(minecraft_dict.items(), key = lambda x: int(x[1]['player']), reverse=True)
            minecraft_dict={}
            for i in new:
                print("hello ",i)
                minecraft_dict.update({i[0]:i[1]})
                print('hey',minecraft_dict)
        time.sleep(15*60)
        

@login_required(login_url="login")
def home(request):
    if 'q' in request.GET:
        server_dict={}
        q=request.GET['q']
        for ip,ip_dict in minecraft_dict.items():
            if ip.find(q.lower())!=-1 or ip.find(q.upper())!=-1:
                server_dict.update({ip:ip_dict})
                ip=ip[1]
        user_object = User.objects.get(username=request.user.username)
        try:
            user_profile = Profile.objects.get(user=user_object)
        except:
            user_profile = Server_Page.objects.get(user=user_object)
        posts = Post.objects.all()
        users= Profile.objects.all()
        return render(request,'test.html',{"mydict":server_dict,'user_profile':user_profile,'posts':posts,'users':users})
    else:
        minecraft_dict
        t1 = threading.Thread(target=minecraft_dict_update, args=())
        t1.start()
        t2 = threading.Thread(target=player_time, args=())
        t2.start()
        user_object = User.objects.get(username=request.user.username)
        try:
            user_profile = Profile.objects.get(user=user_object)
        except:
            user_profile = Server_Page.objects.get(user=user_object)
        posts = Post.objects.all()
        users= Profile.objects.all()
    return render(request,'test.html',{"mydict":minecraft_dict,'user_profile':user_profile,'posts':posts,'users':users})

@login_required(login_url="login")
def statistic(request):
    mydict={}
    connect_SQL=sqlite3.connect('MineBook\\db.sqlite3')
    c =connect_SQL.cursor()
    c.execute("SELECT server_name FROM app_server_page")
    names= c.fetchall()
    for servers in names:
        for server in servers:
            max=c.execute(f"SELECT name,MAX(players),time FROM app_status where name='{server}'")
            max=max.fetchall()
            min=c.execute(f"SELECT name,MIN(players),time FROM app_status where name='{server}'")
            min=min.fetchall()
            for i in max :
                for g in min:
                    print(i)
                    print(g)
                    if i[0]==g[0]:
                        mydict.update({i[0]:{'Maxplayer':i[1],'hightime':i[2],'Minplayer':g[1],'lowtime':g[2]}})
                        print(mydict)
    return render(request,'statistic.html',{'mydict':mydict})

def join(request):
    if request.method == "POST":
        passwd = request.POST['passwd']
        Check_password = request.POST['Check_password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        mydict={'first_name':first_name,'last_name':last_name,'user_name':user_name,'email':email,'passwd':passwd}
        if passwd=="":
            messages.success(request,("You forgot to enter a Password! Please Try Again!"))
            return render(request,'join.html',mydict)
        if Check_password=="":
            messages.success(request,("You forgot to enter a Check Password! Please Try Again!"))
            return render(request,'join.html',mydict)
        if passwd != Check_password:
            messages.success(request,("The passwords do not match! Please Try Again!"))
            return render(request,'join.html',mydict)
        if first_name=="":
            messages.success(request,("You forgot to enter a first name! Please Try Again!"))
            return render(request,'join.html',mydict)
        if last_name=="":
            messages.success(request,("You forgot to enter a last name! Please Try Again!"))
            return render(request,'join.html',mydict)
        if user_name=="":
            messages.success(request,("You forgot to enter a user name! Please Try Again!"))
            return render(request,'join.html',mydict)
        if email=="":
            messages.success(request,("You forgot to enter a email name! Please Try Again!"))
            return render(request,'join.html',mydict)
        if passwd == Check_password:
            if User.objects.filter(email=email):
                messages.success(request,("Your email are already used! Please Try Again!"))
                return render(request,'join.html',mydict)
            if User.objects.filter(username=user_name):
                messages.success(request,("Your user name are already used! Please Try Again!"))
                return render(request,'join.html',mydict)
            else:
                user = User.objects.create_user(username=user_name,email=email,password=passwd,first_name=first_name,last_name=last_name)
                user.save()
                user_login(request)
                user_model = User.objects.get(username=user_name)
                new_profile=Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                messages.success(request,("Your Register Has been submitted successfuly, Have fun in MineBook!"))
                return redirect('settings')
        return redirect('')
    else:
        return render(request,'join.html',{})


def user_login(request):
    if request.method == "POST":
        user_name = request.POST['user_name']   
        passwd = request.POST['passwd']
        mydict={'user_name':user_name}
        user = authenticate(username=user_name, password=passwd)
        if user is not None:
            # the password verified for the user
            login(request, user)
            messages.success(request,("Your login is succses!"))
            return redirect('')
        if passwd=="":
            messages.success(request,("You forgot to enter a Password! Please Try Again!"))
            return render(request,'login.html',mydict)
        if user_name=="":
            messages.success(request,("You forgot to enter a user name! Please Try Again!"))
            return render(request,'login.html',mydict)
        if user is None:
            messages.success(request,("Your User name or Password are worng! Please Try Again!"))
    return render(request,'login.html',{})

@login_required(login_url="login")
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    return render(request,'logout.html',{})


def serverReg(request):
    if request.method == "POST":
        passwd = request.POST['passwd']
        Check_password = request.POST['Check_password']
        Server_name = request.POST['user_name']
        Server_IP = request.POST['Server_IP']
        email = request.POST['email']
        mydict={'Server_name':Server_name,'Server_IP':Server_IP,'email':email,'passwd':passwd}
        if passwd=="":
            messages.success(request,("You forgot to enter a Password! Please Try Again!"))
            return render(request,'serverReg.html',mydict)
        if Check_password=="":
            messages.success(request,("You forgot to enter a Check Password! Please Try Again!"))
            return render(request,'serverReg.html',mydict)
        if passwd != Check_password:
            messages.success(request,("The Passwords do not match! Please Try Again!"))
            return render(request,'serverReg.html',mydict)
        if Server_name=="":
            messages.success(request,("You forgot to enter a Server name! Please Try Again!"))
            return render(request,'serverReg.html',mydict)
        if Server_IP=="":
            messages.success(request,("You forgot to enter a IP! Please Try Again!"))
            return render(request,'serverReg.html',mydict)
        if email=="":
            messages.success(request,("You forgot to enter a email name! Please Try Again!"))
            return render(request,'serverReg.html',mydict)
        if passwd == Check_password:
            if User.objects.filter(email=email):
                messages.success(request,("Your email are already used! Please Try Again!"))
                return render(request,'serverReg.html',mydict)
            if User.objects.filter(username=Server_name):
                messages.success(request,("Your Server name are already used! Please Try Again!"))
                return render(request,'serverReg.html',mydict)
            else:
                user = User.objects.create_user(username=Server_name,email=email,password=passwd)
                user.save()
                user_login(request)
                user_model = User.objects.get(username=Server_name)
                new_server_page=Server_Page.objects.create(user=user_model,id_user=user_model.id,ip=Server_IP,server_name=Server_name)
                new_server_page.save()
                messages.success(request,("Your Register Has been submitted successfuly, Have fun in MineBook!"))
                return redirect('settings')
        return redirect('')
        
    else:
        return render(request,'serverReg.html',{})


@login_required(login_url="login")
def servers_page(request,pk):
    user_object=User.objects.get(username=pk)
    user_profile = Server_Page.objects.get(user=user_object)
    # user_posts = Post.objects.filter(user=pk)
    # user_posts_lenght= len(user_posts)
    context = {
        'user_object':user_object,
        'user_profile' : user_profile,
        # 'user_posts':user_posts,
        # 'user_posts_lenght',user_posts_lenght,
    }
    return render(request,"profile.html",context)


def info(request):
    return render(request,"info.html")

@login_required(login_url="login")
def settings(request):
    a=0
    try:
        user_profile = Profile.objects.get(user=request.user)
        a=0
    except:
        user_profile = Server_Page.objects.get(user=request.user)
        a=1
    if request.method == "POST":
        if request.FILES.get("image") == None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']
            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        if request.FILES.get("image") != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']
            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        return redirect("settings")
    return render(request,"settings.html",{"user_profile":user_profile,'a':a})

@login_required(login_url="login")
def proflie_page(request,pk):
    user_object=User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    # user_posts = Post.objects.filter(user=pk)
    # user_posts_lenght= len(user_posts)
    context = {
        'user_object':user_object,
        'user_profile' : user_profile,
        # 'user_posts':user_posts,
        # 'user_posts_lenght',user_posts_lenght,
    }
    return render(request,"profile.html",context)

@login_required(login_url="login")
def upload(request):
    if request.method == 'POST':
        user = request.user.username
        img = request.FILES.get('image_upload')
        caption = request.POST['caption']
        locaion = request.POST['location']

        new_post= Post.objects.create(user=user,img=img,caption=caption,locaion=locaion)
        new_post.save()
        return redirect('')
    else:
        return redirect('')
