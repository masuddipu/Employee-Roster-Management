from django.urls import path

from . import views

app_name = 'roster'

urlpatterns = [
    path('manage-emp/', views.ManageEmployee.as_view(), name='man_emp'),
    path('manage-client/', views.ManageClient.as_view(), name='man_client'),
    path('emp-list/', views.EmployeeListView.as_view(), name='emp_list'),
    path('client-list/', views.ClientListView.as_view(), name='client_list'),
    path('emp-details/<int:pk>/', views.UserDetailView.as_view(), name='u_detail'),
]
