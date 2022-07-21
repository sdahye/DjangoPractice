from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.hello),
    path('var01', views.variable01),
    path('var02', views.variable02),
    path('for', views.forLoop),
    path('if01', views.if01),
    path('if02', views.if02),
]