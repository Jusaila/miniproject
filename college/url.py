from django.conf.urls import url
from college import views

urlpatterns=[
    url('post_college/', views.colg),
    url('view_college/', views.viewclg)
]