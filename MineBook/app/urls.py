
from django.urls import path
from app import views


urlpatterns = [
    path('',views.home,name=''),
    path('join',views.join,name='join'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('serverReg',views.serverReg,name='serverReg'),
    path('ServerPage/<str:pk>',views.servers_page,name='Servers_page'),
    path('Profile/<str:pk>',views.proflie_page,name='profile_page'),
    path('statistics',views.statistic,name='statistic'),
    path('info',views.info,name='info'),
    path('settings',views.settings,name='settings'),
    path('upload',views.upload,name='upload'),
    path('deletepost',views.deletepost,name='deletepost'),
    path('like-post',views.likePost,name='likePost')
]
