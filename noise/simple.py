import progressbar
import random
import numpy as np

from utils import set_widgets


def simple(height: int = 500, width: int = 500):
    result = []
    widgets = set_widgets('Generating noise', height)
    with progressbar.ProgressBar(max_value=height, widgets=widgets) as bar:
        for row in range(0, height):
            bar.update(row)
            temp = []
            for col in range(0, width):
                temp.append(random.random())
            result.append(temp)
    return np.array(result)
