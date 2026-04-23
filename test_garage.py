import pytest
from garage import enter_garage

def test_enter_garage_basic(garage):
    assert enter_garage(garage, 10, 1) == garage

def test_enter_garage_invalid_hour(garage):
    with pytest.raises(TypeError):
        assert enter_garage(garage, 9, "6")

def test_enter_garage_car_already_in_garage(garage):
    with pytest.raises(ValueError):
        enter_garage(garage, 1, 3)
        assert enter_garage(garage, 1, 4)