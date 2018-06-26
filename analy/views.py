from django.shortcuts import render
from . next_day import w,t,nday,h,p
from django.contrib.auth.models import User
from . yahoo import  climate #import climate.time,temp,wind_dir,wind_speed,sunraise,humidity,presure,visibility
from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from django.views.generic.edit import FormView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .form import Signupform, Signinform, Resetform, UserDetail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . models import weather_data,pre



def data(request):
    return render(request, 'water\\index.html', {'username': request.user.username})

def partners(request):
    return render(request, 'analy\patners.html', {'username': request.user.username})

def about(request):
    return render(request, 'analy\\about.html', {'username': request.user.username})

def graph(request):
    data = weather_data.objects.all()
    return render(request, 'analy\chart1.html',{'temp': data})

def pregraph(request):
    data = weather_data.objects.all()
    return render(request, 'analy\chart4.html',{'temp': data})

def humgraph(request):
    data = weather_data.objects.all()
    return render(request, 'analy\charth.html',{'temp': data})

def visigraph(request):
    data = weather_data.objects.all()
    return render(request, 'analy\chartv.html',{'temp': data})

def sig(request):
    context = {'form': Signinform(), 'pad': '30', 'val': 'Login', 'nam': 'signin', 'new': True}
    form = Signinform(request.POST)
    if request.user.is_authenticated():
        print("login")


    if request.method == 'POST' and form.is_valid():
        if 'signin' in request.POST:
            username1 = form.cleaned_data['user_name']
            password1 = form.cleaned_data['password']
            user = authenticate(request, username=username1, password=password1)
            if user is not None:
                login(request, user)

                return HttpResponse('login sucess')
            else:
                return HttpResponse('login no possible')

    else:

        return render(request, 'analy\sign.html',context)



def graphwind(request):
    data = weather_data.objects.all()
    return render(request, 'analy\chart2.html',{'temp': data})



def post(request):
    form = Signupform(request.POST)

    if request.method == 'POST' and form.is_valid():
        if 'signup' in request.POST:
            username = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, email, password)
            user.last_name = lastname
            user.first_name = firstname
            data1 = user.save()
            print(data1)
            return render(request, 'vv/index.html', {'val': 'singup', 'nam': 'singup'})

        if 'signin' in request.POST:
            username = form.cleaned_data['user_name']
            password = form.cleaned_data['last_name']

            return render(request, 'vv/templates/water/form.html')
        if 'change' in request.POST:
            username = form.cleaned_data['user_name']
            password = form.cleaned_data['last_name']

            return render(request, 'vv/templates/water/form.html')
    else:
        query1 = ['signup', 'signin', 'change']
        return render(request, 'vv/templates/water/form.html', {'form': Signupform(), 'val': 'signup', 'nam': 'signup'})


def log_in(request):
    context = {'form': Signinform(), 'pad': '30', 'val': 'Login', 'nam': 'signin', 'new': True}
    form = Signinform(request.POST)

    if request.method == 'POST' and form.is_valid():
        if 'signin' in request.POST:
            username1 = form.cleaned_data['user_name']
            password1 = form.cleaned_data['password']
            user = authenticate(request, username=username1, password=password1)
            if user is not None:
                login(request, user)

                return HttpResponse('login sucess')
            else:
                return HttpResponse('login no possible')

    else:

        return render(request, 'analy/sign.html', context)


def log_out(request):
    logout(request)
    return HttpResponse('logout sucess')


def signup(request):
    context = {'form': Signupform(), 'pad': '7', 'val': 'signup', 'nam': 'signup'}
    form = Signupform(request.POST)

    if request.method == 'POST' and form.is_valid():
        if 'signup' in request.POST:
            username = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, email, password)
            user.last_name = lastname
            user.first_name = firstname
            data1 = user.save()
            return HttpResponse('signup sucess')

    else:

        return render(request, 'analy/form.html', context)


def change(request):
    context = {'form': Resetform(), 'val': 'Reset password', 'nam': 'change'}
    form = Resetform(request.POST)

    if request.method == 'POST' and form.is_valid():
        if 'change' in request.POST:
            umail = form.cleaned_data['email']
            return HttpResponse('reset your password success fully')

    else:

        return render(request, 'vv/templates/water/form.html', context)



def map(request):
    data = weather_data.objects.all()[::-1]
   # Reserved.objects.filter(client=client_id).order_by('-check_in')
    return render(request,'analy/index.html',{'username':request.user.username,'temp':data})

def home(request):
    data = weather_data.objects.all()
    return render(request,'analy/home.html',{'username':request.user.username,'temp':data})

def anal(request):
    data = weather_data.objects.all()
    return render(request,'analy/anal.html',{'username':request.user.username,'temp':data})



# Create your views here.
def dash(request):
    citis=['nagercoil','thirunelveli','chennai','coimbatore','madurai','pollachi','trichy','tuticorin','salem','erode','theni']

    
    t = str(datetime.now())
    #z = weather_data.objects.latest('time')



        #w = weather_data(place='nagercoil',wind_speed=climate.wind_speed,wind_direction=wind_dir,time=t[11:16],temp=temp,astronomy=sunraise,date=date,presure=presure,humidity=humidity,visibility=visibility)
        #w.save()
    #climate()
   # return render(request,'analy/dash.html',{'time': datetime.now(),'temp': weather_data.objects.all(),'user':request.user.username})
    return render(request, 'analy/home.html', {'username': request.user.username, 'temp': data})

def test1(request,data):
    return HttpResponse(data)

def choose(request):
    pre.objects.all().delete()

    for k in range(len(w)):
        k = int(k)
        d = pre(temp = t[k],date=nday[k],wind =w[k],presure =p[k],humidity=h[k])
        d.save()
    place = ''
    citis =['Nagercoil', 'Tirunelveli', 'Chennai', 'Coimbatore', 'Madurai','Tiruchirappalli','Tuticorin','Salem', 'Erode', 'Theni']
    if 'city' in request.GET:
        place = request.GET.get('place')
        data = weather_data.objects.filter(place=place)
        dataf = pre.objects.all();
        return render(request, 'analy/weather.html', {'username': request.user.username, 'temp': data,'cities':citis,'place': place,'f':dataf})

    return render(request,'analy/weather.html',{'cities':citis,'place': place})