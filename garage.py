
def enter_garage(garage, car_id, entry_hour):
    if not isinstance(entry_hour, int):
        raise TypeError("EntryHour must be a int")
    return garage

def exit_garage(garage, car_id):
    pass

def get_available_spots(garage):
    pass

def calculate_fee(hours, rate):
    pass