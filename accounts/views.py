from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

# SignUpView.
class SignUpView(CreateView):
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
