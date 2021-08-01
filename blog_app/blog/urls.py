from . import views
from django.urls import path

# app_name = 'blog_urls'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('form_1',views.forms_1,name='form_1'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]