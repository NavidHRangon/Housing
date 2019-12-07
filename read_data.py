import pandas as pd
import matplotlib.pyplot as plt
housing = pd.read_csv('https://raw.githubusercontent.com/NavidHRangon/DATA/master/housing.csv')

housing.head()
housing.info()
housing.describe()
housing['ocean_proximity'].value_counts()
housing.hist(bins=50,figsize=(30,20))