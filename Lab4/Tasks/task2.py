from sklearn.preprocessing import MinMaxScaler


def scaler(array):
    return MinMaxScaler().fit_transform(array)


def exec_task(x_train, x_valid, x_test):
    return scaler(x_train), scaler(x_valid), scaler(x_test)
