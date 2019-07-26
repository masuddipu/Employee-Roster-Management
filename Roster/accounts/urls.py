from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('user_login/', views.UserLoginView.as_view(), name='user_login'),
    path('login/', views.AllUserLoginView.as_view(), name='all_login'),
    path('logout/', views.AllUserLogoutView.as_view(), name='all_logout'),
    path('emp_create/', views.EmployeeSignUpView.as_view(), name='emp_create'),
    path('client_create/', views.ClientSignUpView.as_view(), name='client_create'),
    path('update/<int:pk>/', views.UserUpdate.as_view(), name='update'),
]
