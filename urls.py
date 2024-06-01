from django.urls import path
from .import views
urlpatterns=[
    path('',views.home),
    path('setsession/',views.setsession),
    path('getsession/',views.getsession),
    path('setcookie/',views.setcookie),
    path('getcookie/',views.getcookie)
]