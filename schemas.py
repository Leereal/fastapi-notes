from pydantic import BaseModel, ConfigDict
from datetime import datetime

class NoteModel(BaseModel):
    id:str
    title:str
    content:str
    created_at:datetime

    model_config = ConfigDict(
        from_attributes = True
    )

class NoteCreateModel(BaseModel):
    title:str
    content:str

    model_config = ConfigDict(
        from_attributes = True,
        json_schema_extra={
            "example":{
                "title":"Sample Title",
                "content":"Sample content"
            }
        }
    )