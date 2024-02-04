from django.urls import path
from home import views
urlpatterns = [
    path('/', views.home,name="home"),
    path('/blog', views.blog,name="blog"),
    path('/success_page', views.success_page,name="blog"),
    path('/conntact', views.contact,name="blog"),
    path('/about', views.about,name="blog"),
]
