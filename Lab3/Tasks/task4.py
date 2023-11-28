from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics, linear_model
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
from Utils import util


def draw_graph(degrees, test, train):
    plt.plot(degrees, test, '-o', label='test')
    plt.plot(degrees, train, '-0', label='train')
    plt.legend(loc='best')
    plt.savefig('Data/task4.png')
    plt.show()


def exec_task(degrees, train_data, test_data):

    data_x_train, data_y_train = util.get_array_xy(train_data)
    data_x_test, data_y_test = util.get_array_xy(test_data)

    array_test = []
    array_train = []

    for i in range(len(degrees)):
        polynomial_features = PolynomialFeatures(degree=degrees[i], include_bias=False)
        # https://github.com/numpy/numpy/issues/24889
        linear_regression = linear_model.LinearRegression()
        pipeline = Pipeline(
            [
                ("polynomial_features", polynomial_features),
                ("linear_regression", linear_regression),
            ]
        )
        pipeline.fit(data_x_train, data_y_train)

        data_y_answer_test = pipeline.predict(data_x_test)
        data_y_answer_train = pipeline.predict(data_x_train)
        array_test.append(metrics.r2_score(data_y_test, data_y_answer_test))
        array_train.append(metrics.r2_score(data_y_train, data_y_answer_train))

    draw_graph(degrees, array_test, array_train)
