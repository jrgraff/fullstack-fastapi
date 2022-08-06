from fastapi.testclient import TestClient

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