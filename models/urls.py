from django.urls import path, include
from .views import *
urlpatterns = [
    path('people/',  PeopleListView.as_view()),
    path('roles/', PeopleListView.as_view()),
    path('families/', FamilyListView.as_view()),
    path('family-media/', FamilyMediaListView.as_view()),
    path('family/<id>/', FamilyDetailView),
    path('person/<id>/', PersonDetailView),
    path('family-media/<id>/', FamilyMediaDetailView),
]
