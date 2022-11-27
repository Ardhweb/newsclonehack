from django.shortcuts import render,redirect

from django.urls import reverse
# Create your views here.
from accounts.forms import LoginForm, UserRegistrationForm \
    ,UserEditForm, ProfileEditForm

from django.views import View

from django.views.generic import View,CreateView

from django.contrib.auth import authenticate, login, logout 
from django.http import request
from django.http import HttpResponse

from .models import Profile


# class UserRegister(CreateView):
#     template_name = "uregister.html"
#     form_class = UserRegistrationForm


#     def get_success_url(self):
#         return reverse('signup')


        
# class LoginView(View):
#     template_name = "login.html"
#     form_class = LoginForm


#     # def get(self, request):
#     #     form = self.form_class
#     #     message  = ''
#     #     return render(request, self.template_name, context={'form':form, 'message':message})



#     def post(self,request):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect(reverse('home'))




#Function

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                        username=cd['username'],
                                        password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    
        
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid ():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                                user_form.cleaned_data['password'])
            new_user.save()
            #Profile
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request,'register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'uregister.html',{'user_form': user_form})