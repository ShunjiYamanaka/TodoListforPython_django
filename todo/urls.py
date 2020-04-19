from django.urls import path
from .views import TodoList, TodoDetail, TodoCrate, TodoDelete, TodoUpdate

urlpatterns = [
    path('list/', TodoList.as_view(), name='list'),
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    path('create/', TodoCrate.as_view(), name='create'),
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),#<int:pk>何番目のﾃﾞｰﾀを消すのか
    path('update/<int:pk>', TodoUpdate.as_view(), name='update'),
]
