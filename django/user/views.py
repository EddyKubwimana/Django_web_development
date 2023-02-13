from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .forms import UserRegistrationForm,UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from . import signals
def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':

        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            messages.success(request, f"Your account {username} has been created, you can login !")

            return redirect("login")
        else:
            form = form
            messages.error(request, f'password do not match !')
    return render(request, 'user/register.html', {'form':form})
@login_required
def profile(request):
    if request.method == 'POST':
        try:
            p_form = ProfileUpdateForm(request.POST, request.FILES , instance = request.user.profile)
            u_form = UserUpdateForm(request.POST, instance = request.user)
            

            if (u_form.is_valid() and p_form.is_valid()):
                p_form.save
                u_form.save()
                messages.success(request, " Your profile info has been updated")
                return redirect('profile')

        except:
            u_form = UserUpdateForm(request.POST, instance = request.user)

            if u_form.is_valid():
                u_form.save()
                messages.success(request, " Your profile info has been updated")
                return redirect('profile')


    else: 
        try:
            p_form = ProfileUpdateForm(instance = request.user.profile)
            u_form = UserUpdateForm( instance = request.user)
           
        except:
            u_form = UserUpdateForm( instance = request.user)
    try:
        context = {
                   "p_form": p_form,
                  "u_form": u_form }
    
        return render (request, 'user/profile.html', context )
    except:
        context = {
                  "u_form": u_form
                  }
        return render (request, 'user/profile.html', context )


    