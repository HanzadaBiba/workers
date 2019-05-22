from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from account.forms import LoginForm,UserRegistrationForm
from account.models import Profile
from workers.models import Workers
@login_required
def admin_home(request,id):
    profile = get_object_or_404(Profile, user__id=id)
    departament=profile.departament
    print(departament)
    workers=Workers.objects.filter(deps=departament)
    user = request.user
    return render(request,'admin/admin.html',locals())

def register(request):
    if request.method=='POST':
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            cd=user_form.cleaned_data
            departament=cd['departament']
            position=cd['position']
            new_profile=Profile.objects.create(user=new_user,departament=departament,position=position)
            return render(request,
                          'registration/register_done.html',
                          {'new_user': new_user})
    else:
        user_form=UserRegistrationForm()
    return render(request,'registration/register.html',locals())