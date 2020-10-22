from django.urls import path
from . import views

app_name = 'rentals'
urlpatterns = [
    path('', views.estate_filter, name='filter'),
    path('make_filter/', views.make_filter, name='filter'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('details/<int:pk>/', views.DetailView.as_view(), name='details'),
    path('<int:estate_id>/reserve/', views.reserve, name='reserve'),
]
