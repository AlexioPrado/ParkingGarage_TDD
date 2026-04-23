import pytest

@pytest.fixture
def garage():
    return {"capacity": 10, "cars": {}}

@pytest.fixture
def garage_car():
    return {"capacity": 10, "cars": {1:2, 2:3, 3:4}}