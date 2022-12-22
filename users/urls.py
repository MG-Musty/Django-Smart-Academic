from django.urls import path
from django.template import loader
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("apply", views.apply, name="apply"),
    # URLS for all the prompt my TeacherForm
    path('teacher/', views.teacher_list, name='teacher-list'),
    path('teacher/<int:id>/', views.teacher_detail, name='teacher-detail'),
    path('teacher/add/', views.teacher_create, name='teacher-create'),
    path('teacher/<int:id>/change/', views.teacher_update, name='teacher-update'),
    path('teacher/<int:id>/delete/', views.teacher_delete, name='teacher-delete'),
]