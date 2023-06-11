from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('mark_as_done/<int:id>',views.mark_as_done, name='mark_as_done' ),
    path('undo_mark_as_done/<int:id>', views.undo_mark_as_done, name='undo_mark_as_done'),

    # Edit feature
    path('edit_task/<int:id>/', views.edit_task, name="edit_task"),

    # Delete feature
    path('delete_task/<int:id>/', views.delete_task, name="delete_task")
]