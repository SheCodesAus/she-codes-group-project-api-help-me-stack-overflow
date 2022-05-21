from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    path("", views.StudentsList.as_view()),
    path("<int:pk>/", views.StudentsDetail.as_view()),    
    path("coding-languages/", views.StudentCodingLanguagesList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)