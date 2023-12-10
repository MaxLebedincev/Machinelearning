from sklearn.metrics import r2_score


def exec_task(y_per, y_mlpc, y_test):
    print('Точность обучения модели с помощью Perceptron -', r2_score(y_test, y_per))
    print('Точность обучения модели с помощью MLPClassifier -', r2_score(y_test, y_mlpc))
