from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('create_post/', views.create_post, name='create_post'),
    path('<int:id>/<slug:slug>/', views.post, name='post'),
    path('del/<int:id>/', views.del, name='del'),
]