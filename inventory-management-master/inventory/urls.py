from django.urls import path
from django.conf.urls import url
from . import views
from .views import about_to_expire

urlpatterns = [
    path('inventory/', views.StockListView.as_view(), name='inventory'),
    path('new', views.StockCreateView.as_view(), name='new-stock'),
    path('inventory/stock/<pk>/edit', views.StockUpdateView.as_view(), name='edit-stock'),
    path('stock/<pk>/delete', views.StockDeleteView.as_view(), name='delete-stock'),
    path('about-to-expire/', views.about_to_expire, name='about_to_expire'),
    path('download-csv/', views.download_csv, name='download-csv'),
]