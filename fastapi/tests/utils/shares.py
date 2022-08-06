def create_valid_share():
  return {
    'id': 0,
    'name': 'Petroleo Brasileiro SA',
    'abbreviation': 'PETR4',
    'cnpj': '33000167000101' 
  }

def create_invalid_share(invalid_options=['abbreviation']):
  invalid_share = {
    'id': 0,
    'name': 'Petroleo Brasileiro SA',
    'abbreviation': 'PETR4',
    'cnpj': '33000167000101' 
  }

  if 'abbreviation' in invalid_options:
    invalid_share['abbreviation'] = 'AAAAA'
  
  return invalid_share