
from django.urls import path
from .views import TestView

# register StudentViewset with Router 


urlpatterns = [
    path('',TestView.as_view(),name="get All categories"),
    path('<int:pk>/',TestView.as_view(),name="getSingleCategory"),
]