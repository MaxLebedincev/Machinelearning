import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def get_data():
    colnames = ['TimestampSec', 'TimestampMicroSec',
                'S1_AccX', 'S1_AccY', 'S1_AccZ', 'S1_GyrX', 'S1_GyrY', 'S1_GyrZ', 'S1_MagX', 'S1_MagY', 'S1_MagZ',
                'S1_Q1', 'S1_Q2', 'S1_Q3', 'S1_Q4',
                'S2_AccX', 'S2_AccY', 'S2_AccZ', 'S2_GyrX', 'S2_GyrY', 'S2_GyrZ', 'S2_MagX', 'S2_MagY', 'S2_MagZ',
                'S2_Q1', 'S2_Q2', 'S2_Q3', 'S2_Q4',
                'S3_AccX', 'S3_AccY', 'S3_AccZ', 'S3_GyrX', 'S3_GyrY', 'S3_GyrZ', 'S3_MagX', 'S3_MagY', 'S3_MagZ',
                'S3_Q1', 'S3_Q2', 'S3_Q3', 'S3_Q4',
                'S4_AccX', 'S4_AccY', 'S4_AccZ', 'S4_GyrX', 'S4_GyrY', 'S4_GyrZ', 'S4_MagX', 'S4_MagY', 'S4_MagZ',
                'S4_Q1', 'S4_Q2', 'S4_Q3', 'S4_Q4',
                'S5_AccX', 'S5_AccY', 'S5_AccZ', 'S5_GyrX', 'S5_GyrY', 'S5_GyrZ', 'S5_MagX', 'S5_MagY', 'S5_MagZ',
                'S5_Q1', 'S5_Q2', 'S5_Q3', 'S5_Q4',
                'S6_AccX', 'S6_AccY', 'S6_AccZ', 'S6_GyrX', 'S6_GyrY', 'S6_GyrZ', 'S6_MagX', 'S6_MagY', 'S6_MagZ',
                'S6_Q1', 'S6_Q2', 'S6_Q3', 'S6_Q4',
                'S7_AccX', 'S7_AccY', 'S7_AccZ', 'S7_GyrX', 'S7_GyrY', 'S7_GyrZ', 'S7_MagX', 'S7_MagY', 'S7_MagZ',
                'S7_Q1', 'S7_Q2', 'S7_Q3', 'S7_Q4',
                'S8_AccX', 'S8_AccY', 'S8_AccZ', 'S8_GyrX', 'S8_GyrY', 'S8_GyrZ', 'S8_MagX', 'S8_MagY', 'S8_MagZ',
                'S8_Q1', 'S8_Q2', 'S8_Q3', 'S8_Q4',
                'S9_AccX', 'S9_AccY', 'S9_AccZ', 'S9_GyrX', 'S9_GyrY', 'S9_GyrZ', 'S9_MagX', 'S9_MagY', 'S9_MagZ',
                'S9_Q1', 'S9_Q2', 'S9_Q3', 'S9_Q4',
                'label']
    data_frame = pd.read_csv('subject12_self-short.log', sep='\t', names=colnames, header=None)
    data_frame.sample(frac=1)
    return data_frame


def array_train_valid_test(data_frame):
    x_train, x_valid, y_train, y_valid = train_test_split(data_frame.iloc[:, 3:15],
                                                          data_frame[['S1_AccX']].astype(np.int64), test_size=0.3)
    x_valid, x_test, y_valid, y_test = train_test_split(x_valid, y_valid, test_size=0.4)
    return x_train, y_train, x_valid, y_valid, x_test, y_test


def exec_task():
    data_frame = get_data()
    return array_train_valid_test(data_frame)
