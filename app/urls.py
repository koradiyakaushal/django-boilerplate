from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'Person'

router = routers.DefaultRouter()
router.register(r'person', views.PersonView)

urlpatterns = [
	path('', include(router.urls)),
]
