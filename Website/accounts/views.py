from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from .forms import LoginForm, RegisterForm 


def User_login(request):
    form = LoginForm()  
    if request.method == 'POST':
        form = LoginForm(request.POST)  
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print('success')
                return redirect('index')
            else:
                print('failed')
                return render(request, 'accounts/user_login.html', {'form': form})
    return render(request, 'accounts/user_login.html', {'form': form})



from django.contrib import messages
def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print("Registration successful")
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('user_login',messages)
        else:
            print('Registration UNsuccessful')
            messages.error(request, 'Registration UNsuccessful. Please check the form and try again.')
    else:
        form = RegisterForm()
    return render(request, 'accounts/user_register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('user_login')



from django.contrib.auth.decorators import login_required
@login_required
def Userprofile(request):
    user = request.user  
    return render(request, 'accounts/show_profile.html', {'user': user})
    

