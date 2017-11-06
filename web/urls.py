from django.conf.urls import url
from web import views



urlpatterns = [
    url(r'^signup/', views.Signup),
    url(r'^index/', views.Index),
    url(r'^login/', views.Login),
    url(r'^home/', views.Home),
    url(r'^admin/', views.Admin),
    url(r'^logout/', views.Logout),
    url(r'^xiangxi/', views.Xiangxi),
]