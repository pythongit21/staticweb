from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        first = request.POST['firstname']
        last = request.POST['lastname']
        mail = request.POST['email']
        user = request.POST['username']
        pswd = request.POST['psd']
        pswd1 = request.POST['cpsd']
        if pswd == pswd1:
            if User.objects.filter(email=mail).exists():
                messages.info(request, "Email already registered")
                return redirect('register')
            elif User.objects.filter(username=user).exists():
                messages.info(request, "username taken")
                return redirect('register')
            else:
                user1 = User.objects.create_user(first_name=first, last_name=last, email=mail, username=user, password=pswd)
                user1.save()
                print("registration succesfull")
                return redirect("login")

        else:
            messages.warning(request, "Password Mismatched")
            return redirect('register')

    return render(request, "register.html")

def loginp(request):
    if request.method=='POST':
        lid = request.POST['eu']
        lps = request.POST['lpsd']
        user = auth.authenticate(username=lid, password=lps)

        if user is not None:
            auth.login(request, user)
            print("logged in")
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')

    return render(request, 'login.html')

def logoutp(request):
    auth.logout(request)
    return redirect('/')