from django.urls import re_path
from .views import home_page, view_list, new_list, add_item

urlpatterns = [
    re_path(r"^$", home_page, name='home'),
    re_path(r'^lists/new$', new_list, name='new_list'),
    re_path(r'^lists/(\d+)/$', view_list, name='view_list'),
    re_path(r'^lists/(\d+)/add_item$', add_item, name='add_item'),
]
