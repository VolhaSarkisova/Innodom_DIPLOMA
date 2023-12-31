from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView


class RegistrationView(FormView):
    template_name = 'users/registration.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('countries')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistrationView, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('countries')
        return super(RegistrationView, self).get(*args, **kwargs)
        

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('countries')

class CustomLogoutView(LogoutView):
    next_page = 'login'


