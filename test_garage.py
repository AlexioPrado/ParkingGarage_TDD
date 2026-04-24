import pytest
from garage import enter_garage, exit_garage, get_available_spots, calculate_fee

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

def test_exit_garage_true(garage_car):
    assert exit_garage(garage_car, 1) == True

#------get_available_spots------

def test_get_available_spots_7(garage_car):
    assert get_available_spots(garage_car) == 7

def test_get_available_spots_4(garage_car2):
    assert get_available_spots(garage_car2) == 4

#------get_available_spots------

@pytest.mark.parametrize("hours, rate, expected", [
    (6, 4, 24),
    (3.745, 2, 7.49),
    (10, 4, 40)
])
def test_calculate_fee_correct_path(hours, rate, expected):
    assert calculate_fee(hours, rate) == expected