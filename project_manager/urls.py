from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register('projects', views.ProjectView, basename='project')




from . import views

app_name = 'project_manager'
urlpatterns = [
    path('user/register/', views.user_registration, name='user-register'),
    path('user/<int:pk>/', views.user_detail, name='user-detail'),
    path('user/login/', TokenObtainPairView.as_view(), name='user-login'),
    path('', include(router.urls)),
    path('projects/<int:pk>/tasks/', views.task_list_create, name='task-list-create'),
    path('tasks/<int:pk>/', views.task_detail, name='task-detail'),
    path('tasks/<int:pk>/comments/', views.comments_list_create, name='comment-list-create'),
    path('comments/<int:pk>/', views.comments_detail, name='comment-detail'),
    
]