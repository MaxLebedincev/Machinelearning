import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import Perceptron


def analysis_learning_rate(x_train, y_train, x_test, y_test):
    learn_rates = ['constant', 'invscaling', 'adaptive']
    learn_rate_inits = np.linspace(0.1, 1, 10)

    for i in range(len(learn_rates)):
        r_score_mlp = []
        for j in learn_rate_inits:
            mlp = MLPClassifier(random_state=1, max_iter=1000, solver='sgd', learning_rate=learn_rates[i],
                                learning_rate_init=j, tol=0.01)
            mlp.fit(x_train, y_train.values.ravel())

            y_pred = mlp.predict(x_test)
            r_score_mlp.append(r2_score(y_test, y_pred))
        plt.plot(learn_rate_inits, r_score_mlp, '-o')
        plt.title(f'MLPClassifier-Learn_rate-{learn_rates[i]}')
        plt.show()


def analysis_reg_param(x_train, y_train, x_test, y_test):
    alphas = np.linspace(0.1, 1, 10)  # alpha
    r_score_perc = []
    r_score_mlp = []
    for i in alphas:
        perc = Perceptron(alpha=i)
        perc.fit(x_train, y_train.values.ravel())
        y_pred = perc.predict(x_test)
        r_score_perc.append(r2_score(y_test, y_pred))

        mlp = MLPClassifier(alpha=i, max_iter=800)
        mlp.fit(x_train, y_train.values.ravel())
        y_pred = mlp.predict(x_test)
        r_score_mlp.append(r2_score(y_test, y_pred))
    plt.plot(alphas, r_score_perc, '-o')
    plt.title('Perceptron-alpha')
    plt.show()
    plt.plot(alphas, r_score_mlp, '-0')
    plt.title('MLPClassifier-alpha')
    plt.show()


def analysis_solver(x_train, y_train, x_test, y_test):
    opt_functions = ['lbfgs', 'sgd', 'adam']  # solver
    r_score_mlp = []
    for i in opt_functions:
        mlp = MLPClassifier(max_iter=1000, solver=i, tol=0.01)
        mlp.fit(x_train, y_train.values.ravel())
        y_pred = mlp.predict(x_test)
        r_score_mlp.append(r2_score(y_test, y_pred))
    plt.plot(opt_functions, r_score_mlp, '-0')
    plt.title('MLPClassifier-opt_fuction')
    plt.show()


def analysis_hidden_layer(x_train, y_train, x_test, y_test):
    mlp = MLPClassifier(max_iter=800, hidden_layer_sizes=(100,150))
    mlp.fit(x_train, y_train.values.ravel())
    y_pred = mlp.predict(x_test)
    print(f'hidden_layer = 2, size = (100,150), Коэффициент детерминации = {r2_score(y_test, y_pred)}')

    mlp = MLPClassifier(max_iter=800, hidden_layer_sizes=(100,150,200,250))
    mlp.fit(x_train, y_train.values.ravel())
    y_pred = mlp.predict(x_test)
    print(f'hidden_layer = 4, size = (100,150,200,250), Коэффициент детерминации = {r2_score(y_test, y_pred)}')


def exec_task(x_train, y_train, x_test, y_test):
    analysis_learning_rate(x_train, y_train, x_test, y_test)
    analysis_reg_param(x_train, y_train, x_test, y_test)
    analysis_solver(x_train, y_train, x_test, y_test)
    analysis_hidden_layer(x_train, y_train, x_test, y_test)
