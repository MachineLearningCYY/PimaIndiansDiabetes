import matplotlib.pyplot as plt
import pandas
from pandas.plotting import scatter_matrix

# Load data from csv
data_path = './data/pima-indians-diabetes.data'
names = ['PregnantTimes', 'PlasmaGlucoseConcentration', 'BloodPressure', 'TricepsSkinFoldThickness', 'SerumInsulin',
         'BodyMassIndex', 'DiabetesPedigree', 'Age', 'Class']
data = pandas.read_csv(data_path, names=names)

scatter_matrix(data)
plt.hist(data['Age'])
plt.show()
