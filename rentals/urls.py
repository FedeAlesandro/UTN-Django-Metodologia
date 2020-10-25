from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'rentals'
urlpatterns = [
    path('', views.estate_filter, name='filter'),
    path('make_filter/', views.make_filter, name='makefilter'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('<int:estate_id>/', views.details, name='details'),
    path('<int:estate_id>/reserve/', views.reserve, name='reserve'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
