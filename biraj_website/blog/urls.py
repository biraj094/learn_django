from django.urls import path
from . import views

urlpatterns = [path('', views.homepage, name="homepage"),
               path('posts', views.posts, name="posts-page"),
               path('posts/<slug:slug>', views.post, name="post-page")
               ]
