from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import create_post
from .views import blog_detail
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('blog_post/', views.blog_post, name='blog_post'),
    path('login/', views.login_view, name='login'),  
    path('home/', views.home, name='home'),  
    path('blog_post/', views.blog_post, name='blog_post'),
    path('create_post/', create_post, name='create_post'),
    path('blog/<int:post_id>/', blog_detail, name='blog_detail'),
    path('post/<int:post_id>/', views.PostView, name='post_view'),
    path('profile/', views.profile_detail, name='profile_detail'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),  # Burada user_id kullanılacak
    path('created_blogs/', views.created_blogs, name='created_blogs'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
