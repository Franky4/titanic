import pandas
import string


def top_words(lst):
    my_dict = {}
    for item in lst:
        my_dict[item] = my_dict.get(item, 0) + 1
    my_dict.pop('Miss')
    my_dict.pop('Mrs')

    my_sort_dict = sorted(my_dict, key=my_dict.get, reverse=True)
    my_sort_value = sorted(my_dict.values(), reverse=True)
    print('TOP-3 имен:')
    i = 1
    for item, value in zip(my_sort_dict[:3], my_sort_value[:3]):
        print('{}: {} - {}'.format(i, item, value))
        i += 1


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

name = data[data.Sex == 'female']['Name']
my_lst = [word.strip(string.punctuation) for i in name for word in i.split()]
top_words(my_lst)

