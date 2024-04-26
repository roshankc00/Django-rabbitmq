
from django.urls import path
from .views import ProductView

# register StudentViewset with Router 


urlpatterns = [
    path('',ProductView.as_view(),name="get All categories"),
    path('<int:pk>/',ProductView.as_view(),name="getSingleCategory"),
]