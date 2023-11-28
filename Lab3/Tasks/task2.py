from sklearn import linear_model
import matplotlib.pyplot as plt
from Utils import util


def create_linear_regression(train_data):
    data_x_train, data_y_train = util.get_array_xy(train_data)
    linear_regression = linear_model.LinearRegression()
    linear_regression.fit(data_x_train, data_y_train)
    return linear_regression


def draw_graph(x, y_test, y_result):
    plt.plot(x, y_test, '.', color='black')
    plt.plot(x, y_result, color='r')
    plt.savefig('Data/task2.png')
    plt.show()


def exec_task(train_data, test_data):
    linear_regression = create_linear_regression(train_data)
    data_x_test, data_y_test = util.get_array_xy(test_data)
    data_y_result = linear_regression.predict(data_x_test)
    draw_graph(data_x_test['motor_UPDRS'], data_y_test, data_y_result)
    return data_y_test, data_y_result
