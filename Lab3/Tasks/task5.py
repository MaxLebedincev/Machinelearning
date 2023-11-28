from Utils import util
from sklearn import metrics, linear_model
import matplotlib.pyplot as plt


def draw_graph(alpha_coefficients, test, train):
    plt.plot(alpha_coefficients, test, '-o', label='test')
    plt.plot(alpha_coefficients, train, '-0', label='train')
    plt.legend(loc='best')
    plt.savefig('Data/task5.png')
    plt.show()


def exec_task(alpha_coefficients, train_data, test_data):

    data_x_train, data_y_train = util.get_array_xy(train_data)
    data_x_test, data_y_test = util.get_array_xy(test_data)

    array_test = []
    array_train = []

    for alpha in alpha_coefficients:
        reg = linear_model.Ridge(alpha=alpha)
        reg.fit(data_x_train, data_y_train)
        data_y_answer_test = reg.predict(data_x_test)
        data_y_answer_train = reg.predict(data_x_train)
        array_test.append(metrics.r2_score(data_y_test, data_y_answer_test))
        array_train.append(metrics.r2_score(data_y_train, data_y_answer_train))

    draw_graph(alpha_coefficients, array_test, array_train)