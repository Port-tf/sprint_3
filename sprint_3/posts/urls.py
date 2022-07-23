from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    # Основной шаблон 
    path('b1/', views.index_1),
    # Дополнительный шаблон 
    path('b2/', views.index_2),
    # Главная страница после создания моделей
    path('', views.poems, name='poems'),
    path('poems/<str:web_name>/', views.poem_author, name='author'),
    path('poem/<int:argument_id>/', views.post_detail, name='poem'),
    path('users/<str:user_name>/', views.poem_user, name='name_user'),
    path('default/', views.default),

]