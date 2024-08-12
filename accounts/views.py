from django.shortcuts import render,redirect
from django.core.mail import send_mail


from .forms import SignupForm,ActivateCodeForm
from .models import Profile
from django.contrib.auth.models import User

def signup(request):
        
        if request.method=='POST':
              form=SignupForm(request.POST)
              if form.is_valid():
                    username=form.cleaned_data['username']
                    email=form.cleaned_data['email']

                    user=form.save(commit=False)
                    user.is_active=False  

                    form.save()  # create user and create new profile
                    profile=Profile.objects.get(user__username=username)
                    # send email to this user with code
                    send_mail(
                    "Activate code",
                    f"Welcome mr {username}\n pls use this code {profile.code}",
                    "r_midoo@yahoo.com",
                    [email],
                    fail_silently=False,
                )
                    
                    return redirect(f'/accounts/{username}/activate')

              
        else:
              form=SignupForm()
        
        return render(request,'accounts/signup.html',{'form':form})
    
        '''

        - create new user
        - stop active this user
        - redirect actiavte html
        - send eamil to this user with code 


        '''
    

def activate_code(request,username):
    profile=Profile.objects.get(user__username=username)
    if request.method=='POST':
          form=ActivateCodeForm(request.POST)
          if form.is_valid():
                code=form.cleaned_data['code']
                if code==profile.code:
                      profile.code=''

                      user=User.objects.get(username=username)
                      user.is_active=True

                      profile.save()
                      user.save()

                      return redirect('/accounts/login')

    else:
          form=ActivateCodeForm()
    return render(request,'accounts/activate_code.html',{'form':form})
    '''
    - take code and check this code with code by user
    - activate this user
    - return login.html

    '''
