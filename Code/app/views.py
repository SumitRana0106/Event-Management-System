from fastapi import APIRouter
from .models import ServiceEventRequest,AppEventRequest, AppEvents, ServiceEvents
from utility.helpers import mongo_doc_to_json

root = APIRouter()

@root.post("/event/app/")
def post_events(event: AppEventRequest):
    result = dict()
    status_code = 200
    result['result'] = "SUCCESS"
    res = Events(event_type=event.event_type,session_id=event.session_id,data=event.data)
    res.save()
    return result

@root.post("/event/service/")
def post_events(event: ServiceEventRequest):
    result = dict()
    status_code = 200
    result['result'] = "SUCCESS"
    print("In save events >>>>>>>")
    
    res = ServiceEvents(api_id=event.api_id,latency=event.latency,data=event.data)
    res.save()

    result['data'] = res.model_dump()
    return result

@root.get("/event/")
def get_events():
    result = dict()
    status_code = 200
    result['result'] = "SUCCESS"
    docs = Events().get_all()
    se_docs = ServiceEvents.get_all()
    
    result['data'] = mongo_doc_to_json(docs)
    result['ServiceEvents'] = mongo_doc_to_json(se_docs)
    return result