from django.urls import path
from . import views

app_name = 'mnist'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('calc/', views.CalcView.as_view(), name='calc'),
    path('upload/', views.UploadView.as_view(), name='upload'),
    path('paint/', views.PaintView.as_view(), name='paint'),
]
