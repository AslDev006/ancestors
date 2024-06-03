from django.urls import path, include
from .views import *
urlpatterns = [
    path('person/',  PeopleListView.as_view()),
    path('roles/', PeopleListView.as_view()),
    path('family/', FamilyListView.as_view()),
    path('family/<id>/', FamilyDetailView),
    path('person/<id>/', PersonDetailView),
]
