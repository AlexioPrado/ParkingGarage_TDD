import pytest
from garage import enter_garage, exit_garage

#------enter_garage------

def test_enter_garage_basic(garage):
    assert enter_garage(garage, 10, 1) == garage

def test_enter_garage_invalid_hour(garage):
    with pytest.raises(TypeError):
        assert enter_garage(garage, 9, "6")

def test_enter_garage_car_already_in_garage(garage):
    with pytest.raises(ValueError):
        enter_garage(garage, 1, 3)
        assert enter_garage(garage, 1, 4)

def test_enter_garage_full(garage):
    with pytest.raises(ValueError):
        for i in range(10):
            enter_garage(garage, i, i)
        assert enter_garage(garage, 11, 11)

#------exit_garage------

def test_exit_garage_id_not_in_garage(garage_car):
    with pytest.raises(KeyError):
        assert exit_garage(garage_car, 4)

