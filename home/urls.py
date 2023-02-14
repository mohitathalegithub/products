
from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('addproduct',views.addproduct,name="addproduct"),
    path('showproduct',views.showproduct,name="showproduct"),
    path('updateproduct',views.updateproduct,name="updateproduct"),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),

    

]
