from django.urls import path
from . import views
urlpatterns = [
    path('',views.signup, name='signup'),
    path('login',views.login, name='login'),
    path('login.html',views.login),
    path('m7m.html',views.search),
    path('h1.html',views.update),
    path('/update',views.update, name='update'),
    path('search/h1.html',views.update),
    path('search/m7m.html',views.search),
    path('add',views.add,name='add'),
    path('index',views.index,name='index'),
    path('remove',views.remove, name='remove')
]