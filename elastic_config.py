from elasticsearch import Elasticsearch

elastic_client = Elasticsearch(['http://localhost:16384'])
INDEX_NAME = 'stream'
DOC_TYPE = 'stream'