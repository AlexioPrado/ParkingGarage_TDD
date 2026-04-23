import pytest

@pytest.fixture
def garage():
    return {"capacity": 10, "cars": {}}