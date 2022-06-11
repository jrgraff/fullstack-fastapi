from pydantic import BaseModel

class Share(BaseModel):
    id: int
    name: str
    abbreviation: str
    cnpj: str