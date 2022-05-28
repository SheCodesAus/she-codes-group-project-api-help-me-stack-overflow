from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('students/', views.StudentsList.as_view()),
    path('students/<int:pk>', views.StudentsDetail.as_view()),
    path('coding-languages', views.StudentCodingLanguagesList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)