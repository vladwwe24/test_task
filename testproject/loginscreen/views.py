from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


def index(request):
    return render(request, 'loginscreen/index.html')


class RegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = '/login/'

    template_name = 'loginscreen/register.html'

    def form_valid(self, form):
        form.save()

        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    success_url = '/'

    template_name = 'loginscreen/login.html'

    def form_valid(self, form):

        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)