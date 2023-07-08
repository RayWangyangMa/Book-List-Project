from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('confirm_add/<str:isbn>/', views.confirm_add, name='confirm_add'),
    path('delete/<int:book_id>/', views.delete, name='delete'),



]
