from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoLogin, TodoRegister, TodoList, TodoDetailJSON, TodoCreate, todoComplete, todoDelete, TodoUpdate
from django.contrib.auth.views import LogoutView


'''
router = DefaultRouter()

router.register('', TodoViewset)

urlpatterns = [
    path('todos/', include(router.urls))
]
'''

urlpatterns = [
    path('login/',TodoLogin.as_view(),name = 'login'),
    path('register/',TodoRegister.as_view(),name='register'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('todos/', TodoList.as_view(), name='todos'),
    path('todos/<int:pk>/', TodoDetailJSON.as_view(), name='todoJSON'),
    path('todos/agregar/', TodoCreate.as_view(), name='agregar'),
    path("todos/eliminar/<int:pk>/",todoDelete,name="eliminar"),
    path('todos/editar/<int:pk>/', TodoUpdate.as_view(), name='editar'),
    path('todos/completar/<int:pk>/', todoComplete, name='completar')

]