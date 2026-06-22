from django.urls import path
from days import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:day_number>', views.dynamic_days_by_number, name='dynamic_days_by_number'),
    path('<str:day>', views.dynamic_days, name='dynamic_days'),
]