from smarthouse.domain import SmartHouse

DEMO_HOUSE = SmartHouse()

# Building house structure
ground_floor = DEMO_HOUSE.register_floor(1)
entrance = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
# TODO: continue registering the remaining floor, rooms and devices

# tests/demo_house.py

from smarthouse.domain import SmartHouse

# Opprett smarthus-objektet
DEMO_HOUSE = SmartHouse()

# Registrer etasjer
ground_floor = DEMO_HOUSE.register_floor(1)
first_floor = DEMO_HOUSE.register_floor(2)

# Registrer rom
entrance = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
living_room = DEMO_HOUSE.register_room(ground_floor, 30.0, "Living Room")
kitchen = DEMO_HOUSE.register_room(ground_floor, 20.0, "Kitchen")

bedroom = DEMO_HOUSE.register_room(first_floor, 15.0, "Bedroom")
bathroom = DEMO_HOUSE.register_room(first_floor, 10.0, "Bathroom")

# Vis info om huset
print("Registered Floors:", [floor.level for floor in DEMO_HOUSE.get_floors()])
print("Registered Rooms:", [room.name for room in DEMO_HOUSE.get_rooms()])
print("Total House Area:", DEMO_HOUSE.get_area(), "square meters")


