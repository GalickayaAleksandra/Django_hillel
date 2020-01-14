from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [

    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    path('', views.IndexView.as_view(), name='index'),

    path('album/add', views.AlbumCreate.as_view(), name='addalbum'),

    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='updatealbum'),

    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='deletealbum'),

    path('register/', views.UserFormView.as_view(), name='register')



]
