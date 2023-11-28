import random
import numpy as np


def shuffle_lines(data_frame):
    data = data_frame.sample(frac=1)
    train_data, test_data = np.split(data, [int(0.8 * len(data))])
    return train_data, test_data


def shuffle_people(data_frame):
    random_array = random.sample(range(1, 43), 6)
    test_data = data_frame[(data_frame['subject#'].isin(random_array))]
    train_data = data_frame[~(data_frame['subject#'].isin(random_array))]
    return train_data, test_data


def exec_task(is_real_case, data_frame):
    test_data, train_data = shuffle_people(data_frame) if is_real_case else shuffle_lines(data_frame)
    test_data.to_csv('Data/test.csv')
    train_data.to_csv('Data/train.csv')
    return train_data, test_data
