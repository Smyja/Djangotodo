from django.urls import path, include
from .views import get_task, create_task, update_task, delete_task



urlpatterns = [
    path('tasks/<int:task_id>/', get_task),
    path('tasks/', create_task),
    path('tasks/<int:task_id>/update/', update_task),
    path('tasks/<int:task_id>/delete/', delete_task),
]
