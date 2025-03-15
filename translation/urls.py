from django.urls import path
from . import views

urlpatterns = [
    path('translate/', views.TranslationReqView.as_view(), name='translate_text'),
]
