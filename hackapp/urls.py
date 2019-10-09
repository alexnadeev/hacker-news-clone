from django.urls import path
from . import views

urlpatterns = [
    #Alex
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    
    #Jason
    path('user/new', views.new_user, name='new_user'),
    path('user/create_user', views.create_user, name='create_user'),
    path('user/view/<user_id>', views.view_user, name='view'),
    path('user/delete_user', views.delete_user, name='delete_user'),

    #Lorenzo
    path('post/create_post', views.create_post, name='create_post'),
    path('post/<post_id>/delete_post', views.delete_post, name='delete_post'),
    path('post/<post_id>', views.view_post, name='view_post'),
    path('post/<post_id>/edit', views.edit_post, name='edit_post'),
]