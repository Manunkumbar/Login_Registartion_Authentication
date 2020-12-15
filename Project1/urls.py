from django.contrib import admin
from django.urls import path,include
from Login import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/',views.dashboardView, name = "dashboard"),
	path('register/', views.registerPage, name="register"),
	path('', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout")
]
