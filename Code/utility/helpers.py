import json

def mongo_doc_to_json(docs:list):
    for doc in docs:
        doc['_id'] = str(doc['_id'])
    
    return docs