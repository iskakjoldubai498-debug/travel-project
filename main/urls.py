from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tours/', views.tours, name='tours_page'),
    path('about/', views.about, name='about'),
    path('tour/<int:pk>/', views.tour_detail, name='tour_detail'),

    # МЫНА УШУЛ САПТЫ КОШ:
    path('callback/', views.callback_request, name='callback_request'),
]