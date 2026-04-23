import pytest
from garage import enter_garage

def test_enter_garage_basic(garage):
    assert enter_garage(garage, 10, 1) == garage
