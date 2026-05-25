from django.urls import path
from django.http import HttpResponse
from recipes.views import home,contato,sobre


urlpatterns = [
    path('', home), # home
    path('sobre/', sobre), # sobre
    path('contato/', contato),
]
