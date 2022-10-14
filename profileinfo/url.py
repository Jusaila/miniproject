from django.conf.urls import url
from profileinfo import views

urlpatterns = [
    url('profileinfo/', views.profileinfo)

]