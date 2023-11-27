from Utils import util


def exec_task(data_frame, path):
    new_data_frame = data_frame[(data_frame['x1'] < data_frame['x1'].mean()) |
                                (data_frame['x2'] < data_frame['x2'].mean())]
    util.print_success(4)
    return new_data_frame.to_csv(path)
