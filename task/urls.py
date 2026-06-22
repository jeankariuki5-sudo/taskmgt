from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

from task.views import TaskViewSet

router = DefaultRouter()
router.register('task', TaskViewSet)

urlpatterns = [
    path('assigned_person', Assigned_personListCreativeView.as_view()),
    path('assigned_person/<int:pk>', Assigned_personDetailView.as_view),
    path('', include(router.urls))
]