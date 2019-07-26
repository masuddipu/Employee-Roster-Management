from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import User

from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView

def indexView(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return render(request, 'roster/admin_home.html')
        if request.user.is_emp:
            return render(request, 'roster/emp_home.html')
        if request.user.is_client:
            return render(request, 'roster/client_home.html')

    return render(request, 'index.html')

class UserLoginView(TemplateView):
    template_name='registration/user_login.html'

class AllUserLoginView(LoginView):
    pass

class AllUserLogoutView(LogoutView):
    pass

class EmployeeSignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Employee'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_emp = True
        user.phone = form.cleaned_data['phone']
        user.location = form.cleaned_data['location']
        if 'profile_pic' in form.cleaned_data:
                print('found it')
                # If yes, then grab it from the POST form reply
                user.profile_pic = form.cleaned_data['profile_pic']
        user.save()
        return redirect('index')

class ClientSignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_client = True
        user.phone = form.cleaned_data['phone']
        user.location = form.cleaned_data['location']
        if 'profile_pic' in form.cleaned_data:
                print('found it')
                # If yes, then grab it from the POST form reply
                user.profile_pic = form.cleaned_data['profile_pic']
        user.save()
        return redirect('index')

class UserUpdate(UpdateView):
    model = User
    fields = ('username', 'email', 'phone', 'location', 'profile_pic')
    template_name = 'registration/signup_form.html'

    success_url = '/app/emp_list/'
