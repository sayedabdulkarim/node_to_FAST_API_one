from pydantic import BaseModel

class Cuisine(BaseModel):
    label: str
    queryType: str
