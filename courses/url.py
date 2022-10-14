from django.conf.urls import url
from courses import views

urlpatterns = [
    url('view_course/', views.view),
    url('post_college/', views.post)

]