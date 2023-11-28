import numpy as np
import pandas as pd
from Tasks import task1, task2, task3, task4, task5

data_frame = pd.read_csv('data.csv')

# закгрузка данных
data = pd.read_csv('data.csv')

# разделение выборки на тренировочную и тестовую
train_data, test_data = task1.exec_task(False, data)

# обучение модели линейной регрессии
y_test, y_answer = task2.exec_task(train_data, test_data)

# проверка точности модели по тестовой выборке
task3.exec_task(y_test, y_answer)

# Построение модели с использованием полиномиальной функции
task4.exec_task([1, 2, 3], train_data, test_data)

# Построение модели с использованием регуляризации
task5.exec_task(np.linspace(0.001, 100, 25), train_data, test_data)