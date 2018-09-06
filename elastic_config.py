from elasticsearch import Elasticsearch

elastic_client = Elasticsearch(['http://52.15.110.231:16384'])
INDEX_NAME = 'stream'
DOC_TYPE = 'stream'