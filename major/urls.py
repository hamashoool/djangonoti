from django.urls import path

from .views import home, noties, noti

urlpatterns = [
    path('', home, name='home'),
    path('noties/', noties, name='noties'),
    path('the-thing/<int:pk>/', noti, name='noti'),
]
