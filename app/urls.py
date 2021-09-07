from django.urls import path
from . import views



urlpatterns = [
              
    path('',views.home, name ='home'),
    path('login/',views.login_view, name = 'login'),
    path('signup/',views.Signup_view),
    path('add-todo/', views.add_todo, name='todo'),
    path('logout/',views.signout),
    path('delete-todo/<int:id>',views.delete_todo),
    path('change-status/<int:id>/<str:status>',views.change_todo),
    
]
