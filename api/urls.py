from django.urls import path
from .views import *

app_name = 'api'
urlpatterns = [
  path('', post_api, name='post_api'),
  path('<int:id>/', post_id_api, name='post_id_api'),
  path('delete/<int:id>/', post_delete_api, name='post_delete_api'),
  path('update/<int:id>/', post_update_api, name='post_update_api'),
]