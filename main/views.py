import csv

from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm, ImportCSVForm
from .utils import *
from .models import Language, Bedroom

# Create your views here.


def index(request):
    return render(request, 'main.html')


def markup(request):
    return render(request, 'markup.html')


def checkup(request):
    return render(request, 'checkup.html')


def upload(request):
    context = {}

    if request.method == 'GET':
        context['form'] = ImportCSVForm()
        return render(request, 'import.html', context=context)
    # POST

    results = []  # Whole data
    langs = []  # Existing languages in file

    decoded_file = request.FILES['csv'].read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    for row in reader:
        results.append(row)
        if row['language'] not in langs:
            langs.append(row['language'])

    # Creating language_key : Language_object_in_db dictionary
    lang_key_obj = {}
    for lang in langs:
        lang_key_obj[lang] = Language.objects.create(name=lang)

    for row in results:
        new_bedroom = Bedroom()
        new_bedroom.description = row['description']
        new_bedroom.keywords = row['keywords']
        new_bedroom.language = lang_key_obj[row['language']]
        new_bedroom.save()

    return HttpResponse('Data Added!')
#
#
# def login(request):
#     return HttpResponse("Login")
#
#
# def register(request):
#     return HttpResponse("Register")


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Registarion")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'auth/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Autorisation")
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    logout(request)
    return redirect('login')
