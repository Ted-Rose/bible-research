from django.urls import path
from . import views

urlpatterns = [
    path('bible/', views.BiblePassageView.as_view(), name='bible-passage'),
]
