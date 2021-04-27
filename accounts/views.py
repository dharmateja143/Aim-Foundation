from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.

def Register(request):  # New user registration
    if request.method == 'POST':
        user_name = request.POST['Candidate_Name']
        user_email = request.POST['Candidate_Emailid']
        user_password = request.POST['Candidate_Password']
        conform_password = request.POST['Candidate_Conformpassword']

        if user_password == conform_password:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, "Username already exits")
                return redirect('Register')
            elif User.objects.filter(email=user_email).exists():
                messages.info(request, "Email already exits")
                return redirect('Register')
            else:
                user = User.objects.create_user(username=user_name, password=user_password,
                                                email=user_email)
                user.save()
                messages.info(request, "Registered successfully")
                return redirect('Login')


        else:
            print("User paswword unmatched")
            messages.info(request, "Password not matched")
            return redirect('Register')
        return redirect('index')
    else:
        return render(request, 'register.html')


def Login(request):  # User Login Function
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            resp_dict = {
                'name': user.username
            }

            return render(request, "index.html", resp_dict)

        else:
            messages.info(request, "invalid credentials")
            return redirect('Login')
    else:
        return render(request, 'login.html')


def logout_user(request):  # Logout Function
    logout(request)
    return render(request, 'logout.html')