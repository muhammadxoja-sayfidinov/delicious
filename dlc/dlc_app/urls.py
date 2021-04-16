from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('test/', views.test, name="test"),
    path('recept/<int:recept_id>', views.recept, name="recept"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('elements/', views.elements, name="elements"),
    path('blogpost/', views.blogpost, name="blogpost"),
    path('blog_2/', views.blog_2, name="blog_2"),
    path('blog_3/', views.blog_3, name="blog_3"),
    path('burger/', views.burger, name="burger"),
    path('sushi/', views.sushi, name="sushi"),
    path('all/', views.all, name="all"),
]
