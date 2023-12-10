from Tasks import task1, task2, task3, task4, task5

#realdisp+activity+recognition+dataset

x_train, y_train, x_valid, y_valid, x_test, y_test = task1.exec_task()

x_train, x_valid, x_test = task2.exec_task(x_train, x_valid, x_test)

y_perceptron, y_mlpclassifier = task3.exec_task(x_train, y_train, x_test)

task4.exec_task(y_perceptron, y_mlpclassifier, y_test)

task5.exec_task(x_train, y_train, x_test, y_test)

