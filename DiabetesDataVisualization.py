import matplotlib.pyplot as plt
import pandas
from pandas.plotting import scatter_matrix

# Load data from csv
data_path = './data/pima-indians-diabetes.data'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(data_path, names=names)

scatter_matrix(data)
plt.show()
