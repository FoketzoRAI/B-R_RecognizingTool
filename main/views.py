import csv

from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm, ImportCSVForm
from .utils import DataMixin
from .models import Language, Bedroom, Profile, MarkupRes


# Create your views here.


def index(request):
    return render(request, 'main.html')


def markup(request):
    """ Markup view """
    user_profile = Profile.objects.get(user=request.user)

    if user_profile.language is not None:
        language_obj = Language.objects.get(pk=user_profile.language)  # Take language object as user profiles language
    else:  # If user has no profile language - use default language
        language_obj = Language.objects.get(pk=1)

    checked_bedrooms = MarkupRes.objects.filter(user=request.user)
    random_bedroom = Bedroom.objects.filter(language_id=language_obj.id).order_by('?').first()

    # Checking random taken bedroom with already viewed bedroom
    for bedroom in checked_bedrooms:
        if bedroom.bedroom == random_bedroom.id:
            # If the bedroom is the same as checked, take another.
            random_bedroom = Bedroom.objects.filter(language_id=language_obj.id).order_by('?').first()

    context = {
        "bedroom": random_bedroom,
    }

    return render(request, 'markup.html', context=context)


def check(request):
    """ Check the user form & detect checked keywords """

    # Possible keywords
    keys = {
        'double', 'king', 'other', 'queen', 'twin', 'single', 'undefined'
    }
    keywords = ""  # User Keywords
    form_data_keywords = request.POST

    # Detect added user keywords
    for key in keys:
        if key in form_data_keywords:
            keywords += key + " "

    # Create the Markup result and save it to DB
    mr = MarkupRes()
    mr.user = request.user
    mr.bedroom = Bedroom.objects.get(pk=form_data_keywords['bedroom_id'])
    mr.keywords = keywords.strip()
    mr.save()

    return redirect('markup')


def checkup(request):
    return render(request, 'checkup.html')


def upload(request):
    context = {}

    if request.method == 'GET':
        context['form'] = ImportCSVForm()
        return render(request, 'import.html', context=context)
    # POST

    results = []  # Whole data
    languages = []  # Existing languages in file

    decoded_file = request.FILES['csv'].read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)

    # Load data from decoded .csv and detect languages
    for row in reader:
        results.append(row)
        if row['language'] not in languages:
            languages.append(row['language'])

    # Creating language_key : Language_object_in_db dictionary
    lang_key_obj = {}
    for language in languages:
        lang_key_obj[language] = Language.objects.create(name=language)

    # Loading Bedroom data results into DB
    for row in results:
        new_bedroom = Bedroom()
        new_bedroom.description = row['description']
        new_bedroom.keywords = row['keywords']
        new_bedroom.language = lang_key_obj[row['language']]
        new_bedroom.save()

    # On complete redirect to main page
    return redirect('home')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Registration")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'auth/login.html'

    def get_success_url(self):
        """ On successful login """
        return reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Authorisation")
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    logout(request)
    return redirect('home')
