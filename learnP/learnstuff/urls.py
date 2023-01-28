from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name="starting-page"),
    path('posts', views.all_post, name="post-page" ),
  #  path('<int:id>', views.book_detail, name="book-detail" ),
    path('book/<str:slug>/', views.book_detail, name='book_detail'),


]
