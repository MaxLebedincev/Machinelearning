from Tasks import task1, task2, task3, task4, task5
from Utils import const

data_frame = task1.exec_task(f'{const.CONST_DIR}test.csv')
task2.exec_task(data_frame, [
    f'{const.CONST_DIR}CONST_X1.png',
    f'{const.CONST_DIR}CONST_X2.png'
    ])
task3.exec_task(data_frame)
task4.exec_task(data_frame, f'{const.CONST_DIR}test2.csv')
task5.exec_task(data_frame, f'{const.CONST_DIR}3d_model.png')
