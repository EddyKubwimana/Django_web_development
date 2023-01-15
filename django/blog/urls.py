from django.urls import path
from . import views
urlpatterns = [path('', views.Home, name ='blog-home'), path('About/', views.About, name = 'blog-about'),
               path('Published/', views.Published, name= 'blog-published'), path('News/', views.News, name = 'blog-news'),path('Editors/', views.Editors, name = 'blog-editors'),]
