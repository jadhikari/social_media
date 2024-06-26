from re import template
from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_view


app_name = 'user'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_view.LoginView.as_view(template_name = 'user/login.html'), name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name = 'user/logout.html'),name='logout'),
    path('password_change_form/',auth_view.PasswordChangeView.as_view(template_name = 'user/password_change_form.html'),name='password_change_form'),
    path('password_change_done/',auth_view.PasswordChangeDoneView.as_view(template_name = 'user/password_change_done.html'),name='password_change_done'),
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='user/password_reset_form.html',
                                                                email_template_name='user/password_reset_email.html',
                                                                subject_template_name='user/password_reset_subject.txt',
                                                                success_url=reverse_lazy('user:password_reset_done'),
                                                                ),name='password_reset'),
    path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html',
                                                                success_url = reverse_lazy('user:password_reset_complete') 
                                                                ),name='password_reset_confirm'),
    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),

    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]