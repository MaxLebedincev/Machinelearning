def get_x(data_frame):
    return data_frame[[
        'age', 'sex', 'test_time', 'motor_UPDRS', 'Jitter(%)', 'Jitter(Abs)', 'Jitter:RAP',
        'Jitter:PPQ5', 'Jitter:DDP', 'Shimmer', 'Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5',
        'Shimmer:APQ11', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA', 'PPE']]


def get_y(data_frame):
    return data_frame[['total_UPDRS']]


def get_array_xy(data_frame):
    return get_x(data_frame), get_y(data_frame)
