def calc_max_y(vx, vy):
    x, y, y_max = 0, 0, 0
    while x <= target[1] and y >= target[2]:
        x += vx
        y += vy
        if y > y_max:
            y_max = y
        vy -= 1
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        if target[0] <= x <= target[1] and target[2] <= y <= target[3]:
            return y_max
    return False


if __name__ == "__main__":
    target = [175, 227, -134, -79]

    max_y = 0
    counter = 0

    for i in range(target[1] + 1):
        for n in range(target[2], abs(target[2])):
            curr = calc_max_y(i, n)
            if curr is not False:
                counter += 1
                if curr > max_y:
                    max_y = curr

    print(f'Part 1: {max_y}')
    print(f'Part 2: {counter}')
