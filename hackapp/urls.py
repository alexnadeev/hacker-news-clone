from django.contrib.auth import views
from django.urls import path
from django.contrib.auth import views as user_views
from . import views


urlpatterns = [
    #Alex
    #path('login', views.login, name='login'),
    #path('logout', views.logout, name='logout'),
    
    #Jason
    #path('user/new', views.new_user, name='new_user'),
    #path('user/create_user', views.create_user, name='create_user'),
    #path('user/view/<user_id>', views.view_user, name='view'),
    #path('user/delete_user', views.delete_user, name='delete_user'),

    #Lorenzo
    path('home', views.view_post, name="home"),
    path('newest', views.newest, name='newest'),
    path('welcome', views.welcome, name='welcome'),
    path('post/create_post', views.create_post, name='create_post'), 
    path('post/create_post_action', views.create_post_action, name='create_post_action'),
    
    #path('post/<str:slug>', views.view_one_post, name='view_post'),
    #path('post/<post_id>/delete_post', views.delete_post, name='delete_post'),
    #path('post/<post_id>/delete_post_action', views.delete_post_action, name='delete_post_action'),
    
    #path('post/<post_id>/edit', views.edit_post, name='edit_post'),
    
    path('signup/', views.signUp, name='signup'),
    path('login/', user_views.LoginView.as_view(template_name="hackapp/login.html"), name="login"),
    path('logout/', user_views.LogoutView.as_view(template_name="hackapp/logout.html"), name="logout"),
    path('accounts/profile/', views.profile, name='profile')
    
    # path('logout', views.logout, name='logout'),
    
    # #Jason
    # path('user/new', views.new_user, name='new_user'),
    # path('user/create_user', views.create_user, name='create_user'),
    # path('user/view/<user_id>', views.view_user, name='view'),
    # path('user/delete_user', views.delete_user, name='delete_user'),

    # #Lorenzo
    # path('post/create_post', views.create_post, name='create_post'),
    # path('post/<post_id>/delete_post', views.delete_post, name='delete_post'),
    # path('post/<post_id>', views.view_post, name='view_post'),
    # path('post/<post_id>/edit', views.edit_post, name='edit_post'),
]