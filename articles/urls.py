from django.urls import path
from . import views

# crud > urls.py 에서 include() 한 후
# articles/____
urlpatterns = [
    path('new/', views.new),
    path('index/', views.index),
    path('create/', views.create),
]
