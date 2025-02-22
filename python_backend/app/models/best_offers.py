from pydantic import BaseModel

class BestOffer(BaseModel):
    name: str
    abbreviation: str
    image: str
