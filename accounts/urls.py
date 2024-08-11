from django.urls import path
from . import views

urlpatterns = [
    path(route='signup/', view=views.SignUpView.as_view(), name='signup'),
]