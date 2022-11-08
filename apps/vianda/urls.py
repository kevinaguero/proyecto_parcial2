from django.urls import path
from .views import solicitud_vianda_create, vianda_lista


app_name = 'vianda'
urlpatterns = [
    # programa views
    path('', vianda_lista, name='vianda_lista'),
    path('create/', solicitud_vianda_create, name='vianda_create'),
    # path('edit/<int:pk>', programa_edit, name='programa_edit'),
    # path('delete/', programa_delete, name='programa_delete'),
]
