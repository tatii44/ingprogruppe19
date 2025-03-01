class Measurement:
    """
    This class represents a measurement taken from a sensor.
    """

    def __init__(self, timestamp, value, unit):
        self.timestamp = timestamp
        self.value = value
        self.unit = unit

# TODO: Add your own classes here!

# smarthouse/domain.py

class Measurement:
    """Represents a measurement taken from a sensor."""
    def __init__(self, timestamp, value, unit):
        self.timestamp = timestamp
        self.value = value
        self.unit = unit


class Device:
    """Base class for devices like sensors and actuators."""
    def __init__(self, device_id, name):
        self.device_id = device_id
        self.name = name


class Sensor(Device):
    """Represents a sensor that takes measurements."""
    def __init__(self, device_id, name):
        super().__init__(device_id, name)
        self.measurements = []

    def add_measurement(self, measurement):
        self.measurements.append(measurement)


class Actuator(Device):
    """Represents an actuator that can perform actions."""
    def __init__(self, device_id, name):
        super().__init__(device_id, name)
        self.state = None

    def set_state(self, state):
        self.state = state


class Room:
    """Represents a room in the house."""
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)


class Floor:
    """Represents a floor containing multiple rooms."""
    def __init__(self, level):
        self.level = level
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)


class SmartHouse:
    """Main class to manage floors, rooms, and devices."""
    def __init__(self):
        self.floors = []

    def register_floor(self, level):
        floor = Floor(level)
        self.floors.append(floor)
        return floor

    def register_room(self, floor, size, name):
        room = Room(name, size)
        floor.add_room(room)
        return room

    def get_floors(self):
        return self.floors

    def get_rooms(self):
        rooms = [room for floor in self.floors for room in floor.rooms]
        return rooms

    def get_area(self):
        return sum(room.size for floor in self.floors for room in floor.rooms)

class SmartHouse:
    """
    This class serves as the main entity and entry point for the SmartHouse system app.
    Do not delete this class nor its predefined methods since other parts of the
    application may depend on it (you are free to add as many new methods as you like, though).

    The SmartHouse class provides functionality to register rooms and floors (i.e. changing the 
    house's physical layout) as well as register and modify smart devices and their state.
    """

    def register_floor(self, level):
        """
        This method registers a new floor at the given level in the house
        and returns the respective floor object.
        """

    def register_room(self, floor, room_size, room_name = None):
        """
        This methods registers a new room with the given room areal size 
        at the given floor. Optionally the room may be assigned a mnemonic name.
        """
        pass


    def get_floors(self):
        """
        This method returns the list of registered floors in the house.
        The list is ordered by the floor levels, e.g. if the house has 
        registered a basement (level=0), a ground floor (level=1) and a first floor 
        (leve=1), then the resulting list contains these three flors in the above order.
        """
        pass


    def get_rooms(self):
        """
        This methods returns the list of all registered rooms in the house.
        The resulting list has no particular order.
        """
        pass


    def get_area(self):
        """
        This methods return the total area size of the house, i.e. the sum of the area sizes of each room in the house.
        """


    def register_device(self, room, device):
        """
        This methods registers a given device in a given room.
        """
        pass

    
    def get_device(self, device_id):
        """
        This method retrieves a device object via its id.
        """
        pass

