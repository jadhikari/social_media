
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, UserEditForm,ProfileEditForm
from .models import Profile
from post.models import Post


@login_required
def index(request):
    current_user = request.user
    posts = Post.objects.filter(user = current_user)
    profile = Profile.objects.filter(user=current_user).first()
    return render(request, 'user/index.html',{'posts':posts,'profile':profile})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit= False)
            new_user.save()
            Profile.objects.create(user = new_user)
            return redirect('user:login')
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user:index')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    
    return render(request, 'user/edit.html', {'user_form': user_form, 'profile_form': profile_form})





