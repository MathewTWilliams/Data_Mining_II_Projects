# Author: Matt Williams
# Version: 02/21/2023
from random import Random
import math

def simulate_sin():
    total = 1_000_000
    counter = 0
    seed = 42

    rand = Random(seed)
    for _ in range(total):
        x = rand.random() * math.pi
        y = rand.random()

        if y < math.sin(x) :
            counter += 1

    print(f"Simulated Integral of sin(x) from 0->pi using {total} points: {(counter/total) * math.pi}")

if __name__ == "__main__":
    simulate_sin()