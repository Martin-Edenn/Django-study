from django.urls import path, re_path

from .views import index, pageNotFound, addpage, about, contact, login, show_post, show_category

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<slug:cat_slug>/', show_category, name='category')
]
