from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('api/login/',views.user_login,name="login"),
    path('api/register/', views.signup, name="signup"),
    path('api/logout/',views.user_logout,name="logout"),
    path('api/mt/',views.mailtest ,name="mailtest"),
    path('api/admin/',views.admin_data ,name="admin"),
    path('api/events/verify',views.verifyCA,name="verifyCA"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
]
