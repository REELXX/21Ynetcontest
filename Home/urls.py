from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.admin),
    url(r'^overview', views.overview),
    url(r'^voice_detect', views.voice_detect),
    url(r'^Sign_IN&UP', views.Sign),
    url(r'^register', views.register)
    # url(r'touserlist', views.touserlist)

]
