from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})   


@login_required
def profile(request):
	return render(request, 'users/profile.html')



@login_required
def update(request):
	if request.method=='POST':
		u_form = UserUpdateForm(request.POST, 
			instance=request.user)	
		if u_form.is_valid():
			u_form.save()
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)	
	return render(request, 'users/update.html', {'u_form':u_form})