import ormar
from database.config import database, metadata

class Share(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = 'shares'

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100)
    abbreviation: str = ormar.String(max_length=5)
    cnpj: str = ormar.String(max_length=14)