
from tabulate import tabulate
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
# Graphics in SVG format are more sharp and legible
#%config InlineBackend.figure_format = 'svg'
pd.set_option("display.precision", 2)

def printTable(data):
    df = pd.DataFrame(data)
    print(tabulate(df, headers='keys', tablefmt='psql'))

data = pd.read_csv('titanic_train.csv', index_col='PassengerId')
#
# # printTable(data.head(5))
#
# # 1 question
# numberAllPerson = data.count().Sex
# numberFemale = data[data['Sex'] == 'female'].count().Sex
# numberMale = data[data['Sex'] == 'male'].count().Sex
# print(f'Количество пассажиров = {numberAllPerson} | мужчин = {numberMale} | женщин = {numberFemale} |   ')
#
# print('\n')
#
# # 2 question
# numberMiddleClass = data[data['Pclass'] == 2].count().Pclass
# numberMiddleClassFemale = data[(data['Pclass'] == 2) & (data['Sex'] == 'female')].count().Pclass
# numberMiddleClassMale = data[(data['Pclass'] == 2) & (data['Sex'] == 'male')].count().Pclass
# print(f'Количество пассажиров среднего класса = {numberMiddleClass} | мужчин = {numberMiddleClassMale} | женщин = {numberMiddleClassFemale} |')
#
# print('\n')
#
# # 3 question
# numberMiddleClass = data[data['Pclass'] == 2].count().Pclass
# numberMiddleClassFemale = data[(data['Pclass'] == 2) & (data['Sex'] == 'female')].count().Pclass
# numberMiddleClassMale = data[(data['Pclass'] == 2) & (data['Sex'] == 'male')].count().Pclass
# print(f'Количество пассажиров среднего класса = {numberMiddleClass} | мужчин = {numberMiddleClassMale} | женщин = {numberMiddleClassFemale} |')
#
# # 3 question
# print('медиана ', '%.2f' % data['Fare'].median(), ', стандартное отклонение ','%.2f' % data['Fare'].std())
#
# # 4 question
#
# print('\n 4. Правда ли, что средний возраст выживших людей выше, чем у пассажиров, которые в конечном итоге умерли? \n')
#
# deads = data[data['Survived'] == 0]
# mean_age_deads = deads['Age'].mean()
# alives = data[data['Survived'] == 1]
# mean_age_alives = alives['Age'].mean()
# if (mean_age_alives > mean_age_deads):
#     print(
#         'Правда ли, что средний возраст выживших людей выше, чем у пассажиров, которые в конечном итоге умерли? - Да!'
#         '\n(выживших-', mean_age_alives, ', не выживших-', mean_age_deads, ')')
# else:
#     print(
#         'Правда ли, что средний возраст выживших людей выше, чем у пассажиров, которые в конечном итоге умерли? - Нет!'
#         '\n(выживших-', mean_age_alives, ', не выживших-', mean_age_deads, ')')
#
# # 5 question
#
# print('\n 5. Это правда, что пассажиры моложе 30 лет. выжили чаще, чем те, кому больше 60 лет. Каковы доли выживших людей среди молодых и пожилых людей? \n')
#
# young = data[data['Age'] < 30]
# young_procent_alives = len(young[young['Survived'] == 1]) / len(young)
# old = data[data['Age'] > 60]
# old_procent_alives = len(old[old['Survived'] == 1]) / len(old)
#
# print('%.1f' % (young_procent_alives * 100), '% среди молодежи и ', '%.1f' % (old_procent_alives * 100), '% среди пожилых')
#
# # 6 question
#
# print('\n 6. Правда ли, что женщины выживали чаще мужчин? Каковы доли выживших людей среди мужчин и женщин? \n')
#
# women = data[data['Sex'] == 'female']
# women_procent_alives = len(women[women['Survived'] == 1]) / len(women)
# men = data[data['Sex'] == 'male']
# men_procent_alives = len(men[men['Survived'] == 1]) / len(men)
# print('%.1f' % (men_procent_alives * 100), '% среди мужчин и ', '%.1f' % (women_procent_alives * 100), '% среди женщин')

# 7 question

print('\n 7. Какое имя наиболее популярно среди пассажиров мужского пола? \n')

temp = data[data['Sex'] == 'male']['Name'].apply(lambda d : d.split(".")[1]).value_counts().idxmax()


dict = {}

for name in data['Name']:
    arrayName = name.split()
    arrayName[2]
    if (dict.get(arrayName[2], 0) == 0):
        dict.update({arrayName[2]: 1})
    else:
        dict[arrayName[2]] += 1

frequencyName = ''
frequency = 0

for key, value in dict.items():
    if (frequency < value):
        frequencyName = key
        frequency = value

print(f'\n 7 question \n {frequencyName}')


# 8 question
#
# print('\n 8. Как средний возраст мужчин / женщин зависит от Pclass? Выберите все правильные утверждения: \n')
#
# number8questMale = data[(data['Pclass'] == 1) & (data['Sex'] == 'male')]['Age']
# number8anserMale = number8questMale.sum()/len(number8questMale)
#
# print('\n В среднем мужчины 1 класса старше 40 лет \n')
#
# if (number8anserMale > 40):
#     print('Да')
# else:
#     print('Нет')
#
# # нет
# number8questFemale = data[(data['Pclass'] == 1) & (data['Sex'] == 'female')]['Age']
# number8anserFemale = number8questFemale.sum()/len(number8questFemale)
#
# print('\n В среднем женщины 1 класса старше 40 лет \n')
#
# if (number8anserFemale > 40):
#     print('Да')
# else:
#     print('Нет')
#
# # нет
# number8questFemaleAge = data[data['Sex'] == 'female']['Age']
# number8questFemaleAgeSum = number8questFemaleAge.sum()
# number8questFemaleAgeLen = len(number8questFemaleAge)
# number8questMaleAge = data[data['Sex'] == 'male']['Age']
# number8questMaleAgeSum = number8questMaleAge.sum()
# number8questMaleAgeLen = len(number8questMaleAge)
# number8anser3 = (number8questMaleAgeSum/number8questMaleAgeLen) > (number8questFemaleAgeSum/number8questFemaleAgeLen)
#
# print('\n Мужчины всех классов в среднем старше, чем женщины того же класса \n')
#
# if (number8anser3):
#     print('Да')
# else:
#     print('Нет')
#
# # да
# number8questPclass1Age = data[(data['Pclass'] == 1)]['Age']
# number8questPclass2Age = data[(data['Pclass'] == 2)]['Age']
# number8questPclass3Age = data[(data['Pclass'] == 3)]['Age']
#
# quest1 = (number8questPclass1Age.sum()/len(number8questPclass1Age)) > (number8questPclass2Age.sum()/len(number8questPclass2Age))
#
# quest2 = (number8questPclass2Age.sum()/len(number8questPclass2Age)) > (number8questPclass3Age.sum()/len(number8questPclass3Age))
#
# print('\n В среднем, пассажиры первого класса старше, чем пассажиры 2-го класса, которые старше, чем пассажиры 3-го класса. \n')
#
# if (quest1 & quest2):
#     print('Да')
# else:
#     print('Нет')
