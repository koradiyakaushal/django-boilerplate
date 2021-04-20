import requests, json, arrow
from collections import OrderedDict
from datetime import datetime, timedelta

from django.conf.urls import url
from django.http.response import JsonResponse
from django.forms.models import model_to_dict
from django.utils import timezone

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from rest_framework.exceptions import MethodNotAllowed

from drf_yasg.utils import swagger_auto_schema

from .models import Person
from . import swagger_params
from .serializers import PersonSerializer
from .query import *
from conf.settings import DEBUG

INDEX_PERSON = 'person'

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class PersonView(viewsets.ModelViewSet):
	queryset = Person.objects.filter(best_market_cap_rank__lte=500)
	serializer_class = PersonSerializer
	# http_method_names = [m for m in viewsets.ModelViewSet.http_method_names if m not in ['delete']]
	# authentication_classes = [TokenAuthentication, SessionAuthentication]
	permission_classes = (IsAuthenticated, )
	pagination_class = StandardResultsSetPagination
	search_fields = ['name','email']
	filter_backends = (filters.SearchFilter,)

