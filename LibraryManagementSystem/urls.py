from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from core import views as core_views

urlpatterns = [
    path('', core_views.landing, name='landing'),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('login/', core_views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', core_views.register, name='register'),
]
