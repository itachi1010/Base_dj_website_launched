from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "main"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("products/", views.products, name = "products"),
    path("register/", views.register, name="register"),
    #path("user/", views.userpage, name = "userpage"),
    #path("upload/", views.upload, name="upload"),
    #path("contact/", views.contact, name="contact"),
    #path("aboutus/", views.aboutus, name = "aboutus"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path('blog/', views.blog, name='blog'),
    #path("<article_page>", views.article, name = "article"),


    
    
]

