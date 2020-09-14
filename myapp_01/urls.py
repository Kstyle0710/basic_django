
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/download/', views.download),
    path('small_index/', views.samll_index),

]

