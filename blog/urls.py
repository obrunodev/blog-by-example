from blog import views

from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
]
