from django.urls import path , include
from django.contrib.auth import views as auth_views  # django has builtin login view and logout view so we dont have to create it

from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/' , auth_views.LoginView.as_view(template_name = 'accounts/login.html') , name='login') ,
    path('logout/' , auth_views.LogoutView.as_view() , name='logout') , # it will take you to home page after you logout
    path('signup/' , views.SignUp.as_view() , name='signup') ,
    path('password/' , views.change_pass , name='change_password') ,

    # for password reset... can read about reset password here - >  https://simpleisbetterthancomplex.com/tutorial/2016/09/19/how-to-create-password-reset-view.html
#    path('' , include('django.contrib.auth.urls') ) ,

    # OR see in that link
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'accounts/password_reset_form.html' , subject_template_name = 'accounts/password_reset_subject.txt' , email_template_name = 'accounts/password_reset_email.html') , name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_done.html') , name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'accounts/password_reset_confirm.html') , name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = 'accounts/password_reset_complete.html') , name='password_reset_complete'),

#    path('' , include('django.contrib.auth.urls') ) ,

]
