import numpy as np
from sklearn import metrics


def exec_task(data_test, data_result):
    average_percent_difference = 0
    length_data_result = len(data_result)

    for i in range(length_data_result):
        average_percent_difference += abs(((data_result[i][0] / data_test.to_numpy()[i][0]) * 100) - 100)

    print(f'В среднем предсказанные значения отличаются от исходных на {round((average_percent_difference /
                                                                               length_data_result), 2)}')
    print(f'Средняя абсолютная ошибка: {round(metrics.mean_absolute_error(data_test, data_result), 2)}')
    print(f'Среднеквадратичная ошибка: {round(metrics.mean_squared_error(data_test, data_result), 2)}')
    print(f'Среднеквадратичное отклонение: {round(np.sqrt(metrics.mean_absolute_error(data_test, data_result)), 2)}')
    print(f'Коэффициент детерминации: {round(metrics.r2_score(data_test, data_result), 2)}')
