
def enter_garage(garage, car_id, entry_hour):
    if not isinstance(entry_hour, int):
        raise TypeError("EntryHour must be a int")
    for id in garage["cars"].keys():
        if id == car_id:
            raise ValueError("Car already in garage")
    if len(garage["cars"]) >= garage["capacity"]:
        raise ValueError("Garage is full.")

    garage["cars"][car_id] = entry_hour

    return garage

def exit_garage(garage, car_id):
    car_id_checker = 0
    for id in garage["cars"].keys():
        if id == car_id:
            del garage["cars"][car_id]
            return True
        else:
            car_id_checker += 1
    if car_id_checker == len(garage["cars"].keys()):
        raise KeyError("Car not in garage")


def get_available_spots(garage):
    pass

def calculate_fee(hours, rate):
    pass