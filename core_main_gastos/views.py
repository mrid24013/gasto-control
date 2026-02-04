from django.shortcuts import render
from django.views.generic import (
    CreateView
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def home(request):
    return render(request, 'reportes.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "authorization/signup.html"
    success_url = '/login/'