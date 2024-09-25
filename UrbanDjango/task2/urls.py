from django.urls import path
from .views import func_template, ClassTemplate

urlpatterns = [
    path('function/', func_template, name='func_template'),
    path('class/', ClassTemplate.as_view(), name='class_template'),
]