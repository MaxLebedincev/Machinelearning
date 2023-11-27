from Utils import util


def print_max_mean_min(name, col):
    print('Столбец - ' + name)
    print('Максимальное: ' + str(col.max()))
    print('Минимальное:  ' + str(col.min()))
    print('Среднее:      ' + str(col.mean()) + '\n')


def exec_task(data_frame):
    [print_max_mean_min(key, value) for key, value in data_frame.to_dict('series').items()]
    util.print_success(3)
