from django.urls import path
from users.views import login_view, register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name='login'),  
    path('signup/', register, name = 'register'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html')),
    
    #path('update/', update_user, name = 'update_user'),
    #path('update/profile/', update_user_profile, name = 'update_user_profile'),
]