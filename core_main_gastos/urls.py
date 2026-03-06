from django.contrib import admin
from .views import *
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.views.generic import (
    CreateView
)

class CustomLoginView(LoginView):
    template_name = 'Authorization/login.html'
    redirect_authenticated_user = True
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "Authorization/signup.html"
    success_url = '/login/'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/home/')
        return super().dispatch(request, *args, **kwargs)

urlpatterns = [ 
    path('home-permissions/admin/login/', custom_redirect_view),
    path('home-permissions/admin/', admin.site.urls),
    path('home/', home, name= 'home'),
    
    path('', custom_redirect_view, name= 'custom_redirect_view'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    
    #Custom URLs
    path('', include('movimientos_gastos.urls')),
]