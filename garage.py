
def enter_garage(garage, car_id, entry_hour):
    if not isinstance(entry_hour, int):
        raise TypeError("EntryHour must be a int")
    if car_id in garage[car]:
        raise ValueError("Car already in garage")
    if len(garage[car]) >= garage[capacity]:
        raise ValueError("Garage is full.")

    garage[car]["car_id"] = car_id
    garage[car]["entry_hour"] = entry_hour

    return garage

def exit_garage(garage, car_id):
    pass

def get_available_spots(garage):
    pass

def calculate_fee(hours, rate):
    pass