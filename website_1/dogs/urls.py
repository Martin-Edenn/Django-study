from django.urls import path, re_path

from .views import index, categories, archive, index_cats

urlpatterns = [
    path('', index, name='dog_home'),
    path('cats/<int:catid>/', categories),
    path('cats/', index_cats),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]
