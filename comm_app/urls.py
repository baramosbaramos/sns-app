from django.urls import path
from .views import signupfunc, loginfunc, homefunc, roomfunc, logoutfunc

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('home/', homefunc, name='home'),
    path('room/<int:id>', roomfunc, name='room'),
    path('logout/', logoutfunc, name='logout'),
]
