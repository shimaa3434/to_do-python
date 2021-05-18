from .views  import list, edit, delete
from django.urls import path
app_name= 'todo'
urlpatterns = [
    path('list/', list, name= 'list'),
    path('edit/<int:pk>/', edit , name= 'edit'),
    path('delete/<int:pk>/', delete , name= 'delete'),
]
