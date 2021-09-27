from django.urls import path
from .views import IndexView, IndexView2


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('relatorio/', IndexView2.as_view(), name='relatorio')
]
