from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tours/', views.tours, name='tours_page'), # 'tours_page' деп өзгөртүңүз # Бул жер 'tours' болушу керек
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('tour/<int:pk>/', views.tour_detail, name='tour_detail'),
    path('callback/', views.callback_request, name='callback_request'),
]