import matplotlib.pyplot as plt
from Utils import util


def exec_task(data_frame, path):
    fig = plt.figure(figsize=(10, 10))
    ax_3d = fig.add_subplot(projection='3d')
    ax_3d.plot(data_frame['x1'], data_frame['x2'], data_frame['y'])
    plt.savefig(path)
    util.print_success(5)
