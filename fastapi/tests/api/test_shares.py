import asyncio
from fastapi.testclient import TestClient

from models.share import Share
from tests.utils.shares import create_valid_share, create_invalid_share

def test_create_share(client: TestClient) -> None:
  body = create_valid_share()
  response = client.post('/shares/', json=body)
  content = response.json()
  assert response.status_code == 200
  assert content['name'] == body['name']
  assert content['abbreviation'] == body['abbreviation']
  assert content['cnpj'] == body['cnpj']

def test_create_invalid_share(client: TestClient) -> None:
  body = create_invalid_share(['abbreviation'])
  response = client.post('/shares/', json=body)
  assert response.status_code == 422

def test_get_share_by_id(client: TestClient) -> None:
  attributes = create_valid_share()
  share = Share(**attributes)
  loop = asyncio.new_event_loop()
  loop.run_until_complete(share.save())

  response = client.get(f'/shares/{share.id}')
  content = response.json()

  assert response.status_code == 200
  assert content['abbreviation'] == share.abbreviation

def test_get_inexistent_share_by_id(client: TestClient) -> None:
  response = client.get(f'/shares/404')
  content = response.json()

  assert response.status_code == 404