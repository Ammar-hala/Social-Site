from django.shortcuts import render , get_object_or_404 , redirect
from django.views.generic import (TemplateView , ListView , DetailView , CreateView , UpdateView , DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

#for password change
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash #important for changin password
from django.contrib.auth.forms import PasswordChangeForm #built in form

from .models import User
from . import forms
# Create your views here.
class SignUp(CreateView):
    template_name = 'accounts/signup.html'
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login') # once soeomeone has signed up.. take then to login page


def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user , request.POST) #so that form gets the authenticated user


        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request , user) # importatnt cos else after saving form.. user's auth session will be invalidated and he will have to login again
            messages.success(request , 'Your Password was succesfullu updated.')
            return redirect('test')

        else:
            messages.error(request , 'Form not Valid!')

    else:
        form = PasswordChangeForm(request.user)

    return render(request , 'accounts/change_password.html' , {'form' : form} )
