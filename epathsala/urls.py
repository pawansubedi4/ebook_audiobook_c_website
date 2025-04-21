
from django.urls import path,include
from . import views
from .views import authView, home
urlpatterns = [
    # baira ko 
    path('',views.index,name='index'),
    path('index',views.index),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", authView, name="authView"),

    # vitra ko
    path("home", home, name="home"),
    path('uploadm/ebookli', views.ebook_list),
    path('ebookli',views.ebook_list),
    path('uploadm/', views.upload_ebook,),
    path('contact', views.contact),
    path("iamebook",views.iamebook),

    # category
    path('action', views.action),
    path('love', views.love),
    path('horror', views.horror),
    path('thriller', views.thriller),

    #outside ko category
    path('iaction', views.iaction),
    path('ilove', views.ilove),
    path('ihorror', views.ihorror),
    path('ithriller', views.ithriller),

    # audiobook
    path("uploadaudiobook",views.upload_audiobook),
    path("list_audiobook",views.audiobook_list),
    path("audiobook_b",views.audiobook_b),

]