from django.urls import path,include 
from rest_framework import routers
from .import views
from django.conf.urls.static import static
from django.conf import settings

routers = routers.DefaultRouter()
routers.register(r'School',views.SchoolViewset)
routers.register(r'Student',views.SchoolViewset)

urlpatterns = [
    path('', include(routers.urls)),
    path('api_auth/', include('rest_framework.urls',namespace='rest_framework')),
    
]
