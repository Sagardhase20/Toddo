from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/login/'), name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='sign'),
    path('todo/', views.todo_list, name='todo'),
    path('logout/', views.logout_view, name='logout'),
    # path('Task/', views.Task_list, name='task_list'),
]
