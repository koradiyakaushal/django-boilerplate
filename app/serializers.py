from .models import Person
from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import PersonDocument

class PersonDocumentSerializer(DocumentSerializer):
	class Meta:
		document = PersonDocument
		fields = "__all__"

class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields = "__all__"
