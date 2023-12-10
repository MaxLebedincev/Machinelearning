import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def get_data_frame():
    colnames = ['area', 'perimeter', 'compactness', 'length_of_kernel', 'width_of_kernel', 'asymmetry_coefficient',
                'length_of_kernel_groove', 'trash']
    data = pd.read_csv('seeds_dataset.txt', delim_whitespace=True, header=None, names=colnames)
    data = data.sample(frac=1)
    return data


def get_array_after_scaler(data_frame):
    return MinMaxScaler().fit_transform(data_frame.iloc[:, 0:7])


def exec_task():
    data_frame = get_data_frame()
    array = get_array_after_scaler(data_frame)
    return array
