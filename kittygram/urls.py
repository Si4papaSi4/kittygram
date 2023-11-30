from django.urls import path

from cats.views import APICat, APICatDetail

urlpatterns = [
   path('cats/<int:pk>/', APICatDetail.as_view()),
   path('cats/', APICat.as_view()),
]


