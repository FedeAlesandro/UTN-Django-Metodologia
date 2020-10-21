from django.urls import path
from . import views

app_name = 'rentals'
urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.HomeView.as_view(), name='home'),
    path('details/<int:pk>/', views.DetailView.as_view(), name='details'),
]
