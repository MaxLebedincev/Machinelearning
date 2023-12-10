from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import Perceptron


def get_perceptron_result(x_train, y_train, x_test):
    perc = Perceptron()
    perc.fit(x_train, y_train.values.ravel())
    return perc.predict(x_test)


def get_mlpclassifier_result(x_train, y_train, x_test):
    mlp = MLPClassifier(max_iter=1000)
    mlp.fit(x_train, y_train.values.ravel())
    return mlp.predict(x_test)


def exec_task(x_train, y_train, x_test):
    y_perceptron = get_perceptron_result(x_train, y_train, x_test)
    y_mlpclassifier = get_mlpclassifier_result(x_train, y_train, x_test)
    return y_perceptron, y_mlpclassifier


