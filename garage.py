
def enter_garage(garage, car_id, entry_hour):
    if not isinstance(entry_hour, int):
        raise TypeError("EntryHour must be a int")
    if car_id in garage["cars"]["car_id"]:
        raise ValueError("Car already in garage")
    if len(garage["cars"]) >= garage["capacity"]:
        raise ValueError("Garage is full.")

    garage["cars"]["car_id"] = car_id
    garage["cars"]["entry_hour"] = entry_hour

    return garage

def exit_garage(garage, car_id):
    pass

def get_available_spots(garage):
    pass

def calculate_fee(hours, rate):
    pass