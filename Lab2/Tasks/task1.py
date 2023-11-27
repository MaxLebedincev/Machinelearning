from random import randint
import numpy as np
import pandas as pd
from Utils import util
from Utils import const


def init_array():
    array = {
        "x1": np.linspace(randint(1, 5), randint(6, 10), const.CONST_RANGE),
        "x2": np.linspace(randint(1, 5), randint(6, 10), const.CONST_RANGE),
        "y": []
    }

    array["y"] = [util.my_func(x1, x2) for x1, x2 in zip(array["x1"], array["x2"])]

    return array


def save_data_frame(array, path):
    df = pd.DataFrame(array)
    df.to_csv(path)
    return df


def exec_task(path):
    array = init_array()
    data_frame = save_data_frame(array, path)
    util.print_success(1)
    return data_frame
