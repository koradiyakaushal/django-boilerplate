from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry

from elasticsearch_dsl import connections
from conf.settings import ES_URL

connections.create_connection(hosts=[ES_URL], timeout=20)

from .models import Person

person_index = Index('person')
person_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@registry.register_document
class PersonDocument(Document):
    class Index:
        name = "person"
        settings = {
            'number_of_shards': 1,
            "number_of_replicas": 0
        }
    
    class Django:
        model = Person
