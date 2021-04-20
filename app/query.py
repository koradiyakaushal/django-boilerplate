from elasticsearch import Elasticsearch
from conf.settings import ES_URL

INDEX_PERSON = 'person'

es = Elasticsearch(hosts=ES_URL)

def serialize_es_documents(index_name, body):
	# print(body)
	data = es.search(index=index_name, body=body)
	if data['hits']['total']['value'] == 0:
		return [], 0
	return [i['_source'] for i in data['hits']['hits']], data['hits']['total']['value']

def persons(skip, limit, source=False):
	body = {
		"from": skip,
		"size": limit,
		"sort": ["created_at"],
		"query": {"match_all": {}},
	}
	if source:
		body['_source'] = ["id"]
	
	return serialize_es_documents(INDEX_PERSON, body)

