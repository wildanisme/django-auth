from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

class HomeView(View):
    template_name = 'accounts/home.html'

    def get(self, request):
        return render(request, self.template_name)

class CustomLogoutView(LogoutView):
    template_name = 'accounts/login.html'
    next_page = 'login'