from django.shortcuts import render
from app1.forms import UserForm , UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth import authenticate , login , logout
# Create your views here.

def index(request):
    dict = {'name': "pratham" , 'num' : 500}
    return render(request , 'app1/index.html' , context=dict)

@login_required
def special(request):
    return HttpResponse("You are logged in , Nice")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def relative(request):
    return render(request , 'app1/relative.html')



def other(request):
    return render(request , 'app1/other.html')




def users(request):
    registered = False




    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)


        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()


            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors , profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()


    return render(request , 'app1/models.html' , {'user_form':user_form , 'profile_form': profile_form , 'registered':registered})



def user_login(request):
    tries = 0

    if request.method == "POST":
        tries += 1
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username = username , password = password)

        if user:
            if user.is_active:
                login(request , user)
                return render(request , 'app1/login.html' , {'username':username})

            else:
                return HttpResponse("Account Not active")

        else:
            print("Someone tried to login and failed!!")
            return render(request, 'app1/login.html' , {'statement':"Invalid Credentials" , 'tries': tries})

    else:
        return render(request , 'app1/login.html' , {'tries': tries})




