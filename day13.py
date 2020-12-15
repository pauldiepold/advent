with open('./data/day13.txt') as file:
    timestamp = int(file.readline().strip())
    busses = [int(bus) for bus in file.readline().strip().split(',') if bus != 'x']

time_to_wait = timestamp
bus_id = 0
for bus in busses:
    t = bus - timestamp % bus
    if t < time_to_wait:
        time_to_wait = t
        bus_id = bus
print('Teil 1:', time_to_wait * bus_id)


with open('./data/day13.txt') as file:
    timestamp = int(file.readline().strip())
    busses_input = [bus for bus in file.readline().strip().split(',')]

busses = []
for idx, bus in enumerate(busses_input):
    if bus != 'x':
        busses.append([idx, int(bus)])
