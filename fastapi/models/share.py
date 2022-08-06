import ormar
import re
from pydantic import validator
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

    @validator('abbreviation')
    def abbreviation_format_validation(cls, value):
        if not re.compile('^[A-Z]{4}[0-9]{1,2}$').match(value):
            raise ValueError('invalid abbreviation!')
        return value