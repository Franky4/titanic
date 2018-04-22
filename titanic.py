import pandas

data = pandas.read_csv('titanic.csv', index_col='PassengerId')

sex = data['Sex'].value_counts()
print('Мужчин {}, Женщин {}'.format(sex['male'], sex['female']))
survived = data['Survived'].value_counts(normalize=True)
print('Процент выживших {}'.format(round(survived[1]*100,2)))
pclass = data['Pclass'].value_counts(normalize=True)
print('Процент пассажиров первого класса {}'.format(round(pclass[1]*100,2)))

age = data['Age'].describe()['mean']
print('Средний возраст {}, Медиана возраста {}'.format(round(age, 2), round(data['Age'].median())))

slib = data[['SibSp', 'Parch']].corr()
print(round(slib, 2))
