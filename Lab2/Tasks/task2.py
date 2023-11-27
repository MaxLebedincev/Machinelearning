from Utils import util, const
import matplotlib.pyplot as plt


def init_array_y_from_const(is_x1, array):
    if is_x1:
        return [util.my_func(const.CONST_FOR_IMAGE, x) for x in array]
    else:
        return [util.my_func(x, const.CONST_FOR_IMAGE) for x in array]


def create_plot(array_x, array_y, path):
    plt.plot(array_x, array_y)
    [plt.scatter(x, y, color='black', s=15, marker='.') for x, y in zip(array_x, array_y)]
    plt.savefig(path)


def clear_plot():
    plt.clf()


def exec_task(data_frame, paths):
    for flag, array_x, path in zip([True, False], [data_frame['x2'], data_frame['x1']], paths):
        array_y = init_array_y_from_const(flag, array_x)
        create_plot(array_x, array_y, path)
        clear_plot()

    util.print_success(2)
