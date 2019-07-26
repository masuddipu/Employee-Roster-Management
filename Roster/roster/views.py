from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView, ListView
from accounts.decorators import admin_required, emp_required, client_required
from accounts.models import User

# Create your views here.

@method_decorator([login_required, admin_required], name='dispatch')
class ManageEmployee(TemplateView):
    template_name = 'roster/manage_emp.html'

@method_decorator([login_required, admin_required], name='dispatch')
class ManageClient(TemplateView):
    template_name = 'roster/manage_client.html'

@method_decorator([login_required, admin_required], name='dispatch')
class EmployeeListView(ListView):
    context_object_name = 'emplist'
    template_name = 'roster/emp_list.html'
    model = User

    def get_queryset(self):
        queryset = User.objects.filter(is_emp=True)
        return queryset

@method_decorator([login_required, admin_required], name='dispatch')
class ClientListView(ListView):
    context_object_name = 'client_list'
    template_name = 'roster/client_list.html'
    model = User

    def get_queryset(self):
        queryset = User.objects.filter(is_client=True)
        return queryset

# @method_decorator([login_required, admin_required, emp_required, client_required], name='dispatch')
class UserDetailView(DetailView):
    model = User

    template_name = 'roster/user_detail.html'
