from django.urls import path
from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.ProjectsListView.as_view(), name='projects_list'),
    path('detail/<int:pk>', views.ProjectDetailView.as_view(), name='projects_detail'),
    path('like/<int:project_id>', views.like, name='like'),

]
