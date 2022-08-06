import pytest
from models.share import Share
from tests.utils.shares import create_valid_share, create_invalid_share

def test_create_valid_share() -> None:
  attributes = create_valid_share()
  share = Share(**attributes)

def test_create_invalid_share() -> None:
  with pytest.raises(ValueError, match='invalid abbreviation!'):
    attributes = create_invalid_share(['abbreviation'])
    share = Share(**attributes)