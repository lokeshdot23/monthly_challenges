from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='back-to-all-challenges'),
    path("<int:m>", views.monthly_challenges_by_number),
    path('<str:m>', views.monthly_challenge, name='month-challenge'),
]
