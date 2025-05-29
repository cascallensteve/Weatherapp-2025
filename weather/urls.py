from django.urls import path 
from .views import get_weather 
from .import views

# from .views import recommend_activity



urlpatterns = [

      # other paths...
 
    path('', views.index, name='index'),  # Home page as the default
    path('home/', views.home, name='home'),  # Explicit path for home page
    # path('accounts/',('allauth.urls')),  # Include allauth URLs
    path('register/', views.register_view, name='register'),

    path('profile/', views.profile_view, name='profile'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('weather/', views.get_weather, name='weather'),

    path('logout/', views.logout_view, name='logout'),
    # path("recommend/", recommend_activity, name="recommend_activity"),
]



