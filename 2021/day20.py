import numpy as np


def apply_enhancement(image, generation):
    shape = image.shape[0]
    if generation % 2:
        enhanced = np.ones((shape + 2, shape + 2), dtype=int)
        widened = np.ones((shape + 4, shape + 4), dtype=int)
    else:
        enhanced = np.zeros((shape + 2, shape + 2), dtype=int)
        widened = np.zeros((shape + 4, shape + 4), dtype=int)

    widened[2:-2, 2:-2] = image

    for i in range(1, shape + 3):
        for j in range(1, shape + 3):
            binary = widened[i - 1:i + 2, j - 1:j + 2].flatten().tolist()
            number = int((''.join(str(c) for c in binary)), 2)
            enhanced[i - 1, j - 1] = algorithm[number]

    return enhanced


if __name__ == "__main__":
    with open('data/day20.txt') as file:
        algorithm, original = [line for line in file.read().split('\n\n')]

    algorithm = [1 if c == '#' else 0 for c in algorithm]

    original = np.array([[1 if c == '#' else 0 for c in line] for line in original.split('\n')], dtype=int)

    for k in range(50):
        original = apply_enhancement(original, k)
        print(np.count_nonzero(original))
