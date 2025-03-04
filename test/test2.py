import pytest

@pytest.fixture
def sample_data():
    return {'name': 'John', 'age': 25}

def test_user_name(sample_data):
    assert sample_data['name'] == 'John'

def test_user_age(sample_data):
    assert sample_data['age'] == 25