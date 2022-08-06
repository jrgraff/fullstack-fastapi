import os
DATABASE_URL = 'sqlite:///testedb.sqlite'
os.environ['DATABASE_URL'] = DATABASE_URL
os.environ['TEST_DATABASE'] = 'true'

import pytest
from fastapi.testclient import TestClient
from typing import Generator

from api.server import app
from database.create_tables import config_db


@pytest.fixture(scope='function')
def client() -> Generator:
  config_db(DATABASE_URL)
  with TestClient(app) as c:
    yield c