from pydantic import BaseModel, Field
from datetime import datetime
from utility.modelManager import DbBaseModel
import uuid



class AppEventRequest(BaseModel):
    event_type: str = ""
    session_id: str = ""
    page_id: str = ""
    data: dict = {}

class ServiceEventRequest(BaseModel):
    event_type: str = ""
    api_id: str = None
    latency: int = None
    data: dict = {}


# Db Model

def get_time_in_milliseconds():
    return datetime.now().timestamp()


class AppEvents(DbBaseModel):
    table_name = "Events"

    id: str = ""
    event_type: str = ""
    session_id: str = ""
    creation_time: datetime = datetime.now()
    creation_epoch: int = int(datetime.now().timestamp())

    class Meta:
        table_name = "AppEvents"


class ServiceEvents(BaseModel, DbBaseModel):
    event_id: str = Field(default=uuid.uuid4, min_length=4,frozen=True)
    api_id: str = Field(default="", description="unique path/id of service api")
    latency: int = Field(description="api response/latency time in milliseconds")
    creation_time: datetime = Field(default=datetime.now, description="log datetime string")
    creation_epoch: int = Field(default=get_time_in_milliseconds,description="log creation epoch")
    data: dict = Field(default=dict(), description="extra data dictionary")

    class Meta:
        table_name = "ServiceEvents"
    
    def __init__(self,**args):
        super().__init__()