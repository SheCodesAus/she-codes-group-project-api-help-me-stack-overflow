from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('programs/', views.ProgramsList.as_view()),
    path('programs/<int:pk>', views.ProgramsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)