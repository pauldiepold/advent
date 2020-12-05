with open('./data/day05.txt') as file:
    boarding_passes = [''.join(str(int(c == 'B' or c == 'R')) for c in line) for line in file.read().split('\n')]

max_seat_id = 0
seats = []
for boarding_pass in boarding_passes:
    row = int(boarding_pass[0:7], 2)
    column = int(boarding_pass[7:10], 2)
    seat_id = row * 8 + column
    seats.append(seat_id)
    max_seat_id = seat_id if seat_id > max_seat_id else max_seat_id

print('Teil 1: ' + str(max_seat_id))

for i in range(max_seat_id + 1):
    if i - 1 in seats and not (i in seats) and i + 1 in seats:
        print('Teil 2: ' + str(i))

