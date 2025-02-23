from pydantic import BaseModel

class FilterCuisine(BaseModel):
    label: str
    queryType: str
