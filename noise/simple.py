import random
import numpy as np


def simple(height: int = 500, width: int = 500):
    print('Generating simple noise...')
    result = []
    for row in range(0, height):
        temp = []
        for col in range(0, width):
            temp.append(random.random())
        result.append(temp)
    return np.array(result)
