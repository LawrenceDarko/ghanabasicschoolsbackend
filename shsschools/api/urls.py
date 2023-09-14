from django.urls import path
from .views import school_list, school_detail

app_name = 'api'
urlpatterns = [
    path('schools/', school_list, name='school_list'),
    path('schools/<int:pk>/', school_detail, name='school_detail'),
]
